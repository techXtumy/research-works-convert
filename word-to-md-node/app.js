const fs = require("fs-extra");
const path = require("path");
const mammoth = require("mammoth");
const TurndownService = require("turndown");
const { execSync } = require("child_process");

const inputFolder = "./public";
const outputFolder = "./result";
fs.ensureDirSync(outputFolder); 

const turndownService = new TurndownService();

fs.readdirSync(inputFolder).forEach(file => {
    if (file.endsWith(".docx")) {
        const inputPath = path.join(inputFolder, file);
        const outputPath = path.join(outputFolder, file.replace(".docx", ".md"));

        fs.readFile(inputPath, (err, data) => {
            if (err) throw err;

            mammoth.convertToHtml({ buffer: data })
                .then(result => {
                    const html = result.value;

                    const markdown = turndownService.turndown(html);

                    fs.writeFileSync(outputPath, markdown, "utf-8");

                    console.log(`✅ Đã chuyển đổi: ${outputPath}`);

                    try {
                        execSync(`npx markdownlint ${outputPath}`, { stdio: "inherit" });
                    } catch (e) {
                        console.warn(`⚠️ Cảnh báo markdownlint cho ${outputPath}`);
                    }
                })
                .catch(error => console.error(`Lỗi chuyển đổi: ${error.message}`));
        });
    }
});
