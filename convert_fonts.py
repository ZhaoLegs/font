import base64
import os

# 获取脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 字体文件路径
fonts = [
    {
        'name': 'Ola Sans Compact',
        'path': os.path.join(script_dir, 'fonts', 'OlaSansCompactVF.ttf')
    },
    {
        'name': 'Ola Sans Mono',
        'path': os.path.join(script_dir, 'fonts', 'Ola Sans Mono.ttf')
    }
]

def convert_font_to_base64(font_path):
    try:
        with open(font_path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        print(f"Error reading font file {font_path}:", e)
        return None

def generate_font_face_css(font_name, base64_data):
    return f"""@font-face {{
    font-family: '{font_name}';
    src: url(data:font/truetype;charset=utf-8;base64,{base64_data}) format('truetype');
    font-weight: 300 800;
    font-style: normal;
    font-display: swap;
}}
"""

def main():
    css_content = ''
    
    for font in fonts:
        print(f"Processing font: {font['name']}")
        print(f"Font path: {font['path']}")
        base64_data = convert_font_to_base64(font['path'])
        if base64_data:
            css_content += generate_font_face_css(font['name'], base64_data)
            print(f"Successfully converted {font['name']}")
        else:
            print(f"Failed to convert {font['name']}")
    
    output_path = os.path.join(script_dir, 'fontfaces.css')
    with open(output_path, 'w') as f:
        f.write(css_content)
    print(f'Font faces have been converted and saved to {output_path}')

if __name__ == '__main__':
    main()
