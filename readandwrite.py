import re
import jieba

def load(path):
    # 读取文件
    f = open(r'%s' % path, mode='r', encoding='utf-8')
    text = f.read()
    f.close()
    
    # 清理html格式、一部分标点符号、单独占据一行的无空格英文/符号字符串、中文中的空格
    text = re.sub(r'<.*?>', '', text, flags=re.S)
    text = re.sub(r'\s{2,}', '\n', text)
    text = re.sub(r'''[“”‘’"'\(\)\{\}\[\]（）【】《》]''', '', text)
    en_patten = re.compile(r'(^|([\n] *))[a-zA-Z0-9.,;:!\?_&\*\/\-\+\\=↵<>]+(( *[\n])|$)')
    text = en_patten.sub(r'\1\2', text)
    text = en_patten.sub(r'\1\2', text)
    space_patten = re.compile(r'([^a-zA-Z0-9.,!?])[ \t]+([^a-zA-Z0-9.,!?])')
    text = space_patten.sub(r'\1\2', text)
    text = space_patten.sub(r'\1\2', text)

    # 异常处理：文件为空
    if len(text) < 2:
        return 0
    return jieba.cut(text)

# 格式化并输出结果
def output(path, ans):
    f = open(r'%s' % path, mode='w', encoding='utf-8')
    f.write('%.2f' % ans)
    f.close()