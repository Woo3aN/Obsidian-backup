module.exports = async (params) => {
    const { app, obsidian } = params;
    const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);
    if (!view || !view.editor) {
        new obsidian.Notice("⚠️ 请先打开一个 Markdown 笔记再运行脚本");
        return;
    }

    let text = view.editor.getValue();

    // ======================================
    // 1. 处理块级公式 $$ ... $$
    // ======================================
    text = text.replace(/\$\$([\s\S]*?)\$\$/g, (match, formulaContent) => {
        let fixed = formulaContent;

        // 1.1 替换 \left\{ / \right\} 为 GitHub 兼容写法
        fixed = fixed.replace(/\\left\{/g, "\\lbrace");
        fixed = fixed.replace(/\\right\}/g, "\\rbrace");

        // 1.2 把公式内所有换行和多余空格压缩为一行
        fixed = fixed.replace(/\s+/g, " ").trim();

        // 1.3 强制给公式块前后各加一行空行（GitHub 渲染必须）
        return `\n\n$$\n${fixed}\n$$\n\n`;
    });

    // ======================================
    // 2. 处理行内公式 $ ... $
    // ======================================
    text = text.replace(/(?<!\$)\$([^\n$]+?)\$(?!\$)/g, (match, inlineFormula) => {
        let fixed = inlineFormula;

        // 2.1 同样替换 \left\{ / \right\}
        fixed = fixed.replace(/\\left\{/g, "\\lbrace");
        fixed = fixed.replace(/\\right\}/g, "\\rbrace");

        // 2.2 去掉行内公式内的多余空格
        fixed = fixed.replace(/\s+/g, " ").trim();

        // 重新包裹行内公式
        return `$${fixed}$`;
    });

    // ======================================
    // 3. 处理大括号 {} 内的公式（避免换行解析错误）
    // ======================================
    // 匹配公式内的 { ... }，并把内部内容压缩成一行
    text = text.replace(/\{([\s\S]*?)\}/g, (match, inside) => {
        return "{" + inside.replace(/\s+/g, " ").trim() + "}";
    });

    // ======================================
    // 4. 写入修改后的内容
    // ======================================
    view.editor.setValue(text);
    new obsidian.Notice("✅ 所有公式已转为 GitHub 兼容格式！");
};