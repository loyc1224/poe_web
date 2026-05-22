from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Sample POE information - in a real application, you'd get this from an API
poe_data = {
    "classes": ["Marauder", "Duelist", "Ranger", "Shadow", "Witch", "Templar", "Scion"],
    "leagues": ["Standard", "Hardcore", "Temporary League 1", "Temporary League 2"],
    "latest_version": "3.22.0"
}

# Skills data based on the provided images
skills_data = [
    {"chapter": "A1", "progress": "打死西拉克後", "skills": ["熔岩翻騰"], "supports": ["秘能波動輔助"]},
    {"chapter": "A1", "progress": "打破鳥巢後點冰雹之消債送門", "skills": ["機率幻影", "霜凍之蹤"], "supports": ["神聖火舌圖騰", "秘能波動輔助"]},
    {"chapter": "A1", "progress": "醫療箱後", "skills": ["熔岩翻騰", "霜凍之蹤"], "supports": ["元素擴散", "召喚幻影輔助"], "notes": "秘能只需2等"},
    {"chapter": "A1", "progress": "", "skills": ["神聖火舌圖騰"], "supports": ["召喚幻影輔助", "附加閃電傷害"]},
    {"chapter": "A1", "progress": "監獄傳送點", "skills": ["霜凍之蹤"], "supports": ["秘能波動輔助", "燃燒輔助"]},
    {"chapter": "A1", "progress": "", "skills": ["熔岩翻騰"], "supports": ["元素擴散", "燃燒輔助"]},
    {"chapter": "A1", "progress": "", "skills": ["重盾衝鋒"], "supports": ["快速攻擊輔助"], "notes": "快速攻擊女巫不會拿，近戰職業"},
    {"chapter": "A1", "progress": "監獄昇華", "skills": ["活力"], "supports": []},
    {"chapter": "A1", "progress": "女妖前", "skills": ["塊均奔流"], "supports": [], "notes": "額外減益傷害附加 60% 傷害\n火焰曝曬 -25% 火焰抗性"},
    {"chapter": "A2", "progress": "罪孽之殿", "skills": ["灰燼之捷"], "supports": ["閃電之捷"]},
    {"chapter": "A2", "progress": "蜘蛛者巢穴", "skills": ["快速施放"], "supports": ["烈焰衝刺"]},
    {"chapter": "A2", "progress": "蜘蛛者巢穴", "skills": ["重盾衝鋒"], "supports": ["快速攻擊輔助", "暴風之盾"], "notes": "暴風之盾拿法格25%"},
    {"chapter": "A2", "progress": "盜賊營-幫阿莉亞3抗", "skills": ["堅凍"], "supports": []},
    {"chapter": "A2", "progress": "古代封印", "skills": ["信念浪湧"], "supports": []},
    {"chapter": "A2", "progress": "靜謐陵昇華", "skills": [], "supports": []},
    {"chapter": "A3", "progress": "火鋒塔的昇華", "skills": [], "supports": []},
    {"chapter": "A3", "progress": "下水道 拿三親雕像", "skills": [], "supports": []},
    {"chapter": "A3", "progress": "軍石廢墟的昇華", "skills": [], "supports": []},
    {"chapter": "A3", "progress": "激戰廣場 > 奪絲綠之軸 > 到海港 > 拿酥糖", "skills": [], "supports": []},
    {"chapter": "A3", "progress": "找達拉夫人", "skills": [], "supports": []},
    {"chapter": "A3", "progress": "格拉維奇將軍", "skills": ["未日烙印"], "supports": ["燃燒輔助", "元素擴散(A4 38等後換點燃擴散)", "發輝(A4 38等後換換特性)"]},
    
    # New data from the second image
    {"chapter": "A3", "progress": "格拉維奇將軍", "skills": ["旋渦"], "supports": ["快速施放", "秘能波動", "物理波動"]},
    {"chapter": "A3", "progress": "格拉維奇將軍", "skills": ["烈焰之屋"], "supports": ["易燃"]},
    {"chapter": "A3", "progress": "格拉維奇將軍", "skills": ["信念浪湧"], "supports": ["堅定"]},
    {"chapter": "A3", "progress": "月影之殿", "skills": ["圖書館的黃金之頁"], "supports": ["重傷衛詩或譯筆", "快速攻擊"]},
    {"chapter": "A3", "progress": "", "skills": ["圖書館的黃金之頁"], "supports": ["堅定"], "notes": "開始閃電之捷"},
    {"chapter": "A1", "progress": "打死西拉克後", "skills": ["熔岩翻騰"], "supports": ["秘能波動輔助"]},
    {"chapter": "A1", "progress": "打破鳥巢後點冰雹之消債送門", "skills": ["火靈"], "supports": ["秘能波動輔助"]},
    {"chapter": "A1", "progress": "", "skills": ["機率幻影"], "supports": ["神聖火舌圖騰"]},
    {"chapter": "A1", "progress": "", "skills": ["霜凍之蹤"], "supports": ["霜濤之腿"]},
    {"chapter": "A1", "progress": "打完與蛛後水水之後傳送門", "skills": ["火靈"], "supports": ["秘能波動輔助"]},
    {"chapter": "A1", "progress": "", "skills": ["機率幻影"], "supports": ["神聖火舌圖騰"]},
    {"chapter": "A1", "progress": "", "skills": ["霜凍之蹤"], "supports": ["霜濤之腿"]},
    {"chapter": "A1", "progress": "典獄長前", "skills": ["火靈"], "supports": ["火靈軍團輔助", "秘能波動輔助/召喚物傷害"]},
    {"chapter": "A1", "progress": "打完典獄長", "skills": ["火靈"], "supports": ["燃燒輔助", "火靈軍團輔助", "召喚物傷害", "天賦-復仇之靈(自爆)"]},
    {"chapter": "A1", "progress": "", "skills": ["霜濤之腿"], "supports": ["秘能波動輔助"]},
    {"chapter": "A1", "progress": "", "skills": ["烈焰衝刺"], "supports": []},
    {"chapter": "A1", "progress": "", "skills": ["海妖完"], "supports": ["血肉奉獻"]},
    {"chapter": "A2", "progress": "打完罪孽之殿", "skills": ["旋渦"], "supports": []},
    {"chapter": "A2", "progress": "蜘蛛", "skills": ["正火"], "supports": ["元素集中輔助", "活栓輔助", "效能"], "notes": "活栓輔助女巫不會給，要其他職業"},
    {"chapter": "A2", "progress": "蜘蛛", "skills": ["霜濤之腿"], "supports": ["寒冰轉換始輔助", "燃燒輔助"], "notes": "霜濤點滿高+昇華必定點滿+寒冰轉烈焰"},
    {"chapter": "A3", "progress": "火野場", "skills": ["易燃"], "supports": [], "notes": "正火核心重要，女巫拿不到"},
    {"chapter": "A3", "progress": "圖書館的黃金之頁", "skills": ["正火"], "supports": ["元素集中輔助", "極速苦痛輔助", "燃燒傷害輔助", "活栓輔助"]},
    {"chapter": "A4", "progress": "", "skills": ["正火"], "supports": ["元素集中輔助", "極速苦痛輔助", "燃燒傷害輔助", "增加範圍輔助", "活栓輔助"]},
    {"chapter": "A4", "progress": "", "skills": ["火靈"], "supports": ["火靈軍團輔助", "召喚物生命輔助", "釋放輔助（藍）"]}
]

# New data structure for unique items
unique_items_data = [
    {
        "name": "女巫火靈起手",
        "chapter": "A1",
        "notes": "Witch Fire Elemental build starter"
    }
]

@app.route('/')
def home():
    return render_template('index.html', title="Path of Exile Info", poe_data=poe_data)

@app.route('/classes')
def classes():
    return render_template('classes.html', title="POE Classes", classes=poe_data["classes"])

@app.route('/leagues')
def leagues():
    return render_template('leagues.html', title="POE Leagues", leagues=poe_data["leagues"])

@app.route('/skills')
def skills_table():
    return render_template('skills_table.html', title="POE Skills Table", skills=skills_data, unique_items=unique_items_data)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Implement real search functionality here
    results = [item for item in poe_data["classes"] + poe_data["leagues"] if query.lower() in item.lower()]
    return render_template('search.html', title="Search Results", query=query, results=results)

if __name__ == '__main__':
    # Create templates directory and templates before running
    app.run(debug=True)
