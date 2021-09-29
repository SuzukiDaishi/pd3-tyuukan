import glob
from os import name

names = ['p226', 'p230', 'p231', 'p232']
bg_color = ['#bccf3d','#e8a0b8', '#ffc300', '#02c9c9']

def get_sec(base_name, conv_name, mel_or_sp):
    out1 = None
    out2 = None
    with open(f'./mel/output_{base_name}_{conv_name}.txt') as f:
        lines = f.readlines()
        out1 = round(float(lines[0].split(':')[-1]), 2)
        out2 = round(float(lines[1].split(':')[-1]), 2)
    if mel_or_sp == 'sp':
        with open(f'./sp/output_{base_name}_{conv_name}.txt') as f:
            lines = f.readlines()
            out2 = round(float(lines[0].split(':')[-1]), 2)
    return out1, out2

def get_color(base_name):
    return bg_color[names.index(base_name)]

def get_html(base_name, conv_name, secs, mel_or_sp):
    return f'''
<div class="box-wrap" style="background:linear-gradient(to right,{get_color(base_name)} 45%,{get_color(conv_name)} 55%);">
<h2>{ '元論文の手法' if mel_or_sp == 'mel' else '提案手法' }</h2>
<div class="box">
<h3>{base_name}</h3>
<audio src="./original/{base_name}.wav" controls></audio>
<img src="./original/{base_name}_{mel_or_sp}.png" class="photo"/>
</div>
<div class="box-arrow">
<p><b>RTF:</b> {round(secs[1]/secs[0], 2)}</p>
<img src="./images/mark_arrow_right.png" class="photo"/>
</div>
<div class="box">
<div class="audio-box">
<div>
<h3>{conv_name}</h3>
<audio src="./{mel_or_sp}/output_{base_name}_{conv_name}.wav" controls></audio>
</div>
<div>
<h4>目標話者</h4>
<audio src="./original/{conv_name}.wav" controls></audio>
</div>
</div>

<img src="./{mel_or_sp}/output_{base_name}_{conv_name}.png" class="photo"/>
</div>
</div>
'''
out_html = ''

for base_name in names:
    for conv_name in names:
        for mel_or_sp in ['mel', 'sp']:
            secs = get_sec(base_name, conv_name, mel_or_sp)
            out_html += get_html(base_name, conv_name, secs, mel_or_sp).replace('\n','') + '\n'
print(out_html)
    