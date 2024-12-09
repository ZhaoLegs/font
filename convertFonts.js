const fs = require('fs');
const path = require('path');

// 字体文件路径
const fonts = [
    {
        name: 'OlaSansCompactVF',
        path: './fonts/OlaSansCompactVF.ttf'
    },
    {
        name: 'OlaSansMono',
        path: './fonts/Ola Sans Mono.ttf'
    }
];

// 转换字体文件到Base64
function convertFontToBase64(fontPath) {
    try {
        const font = fs.readFileSync(fontPath);
        return font.toString('base64');
    } catch (error) {
        console.error(`Error reading font file ${fontPath}:`, error);
        return null;
    }
}

// 生成CSS @font-face 声明
function generateFontFaceCSS(fontName, base64Data) {
    return `@font-face {
    font-family: '${fontName}';
    src: url(data:font/truetype;charset=utf-8;base64,${base64Data}) format('truetype');
    font-weight: 300 800;
    font-style: normal;
    font-display: swap;
}\n`;
}

// 主函数
function main() {
    let cssContent = '';
    
    fonts.forEach(font => {
        const base64Data = convertFontToBase64(font.path);
        if (base64Data) {
            cssContent += generateFontFaceCSS(font.name, base64Data);
        }
    });

    // 将结果写入到文件
    fs.writeFileSync('fontfaces.css', cssContent);
    console.log('Font faces have been converted and saved to fontfaces.css');
}

main();
