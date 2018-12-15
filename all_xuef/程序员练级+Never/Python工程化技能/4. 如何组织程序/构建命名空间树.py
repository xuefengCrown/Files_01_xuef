
"""
一个名为 acme的应用程序要提供一个知道如何创建 PDF文件的引擎。
它将基于一系列末班文件和一个 MySQL数据库上的查询。
acme应用的3个部分是:
一个 PDF 生成器
一个 SQL引擎
一个模板集合

由此，命名空间树的初稿可能是:
acme
    pdfgen.py
        class PDFGen

    sqlengine.py
        class SQLEngine
    
    templates.py
        class Template


"""
# 第2稿可能是:
# 参见 p116
