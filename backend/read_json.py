import json

f = open('guild_stash.json', encoding='utf-8')
##f = open('stash.json', encoding='utf-8')
re_data = json.load(f)
f.close()

item = re_data["items"]
output = []
for i in item:
    temp = {
        "name": i["typeLine"],
        "values": int(i["properties"][0]["values"][0][0].split("/")[0])
    }
    output.append(temp)

print(output)


####### below transferred to html&js by gpt
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Guild Stash Parser</title>
# </head>
# <body>
#     <h1>Guild Stash Parser</h1>

#     <!-- 輸入框讓用戶貼上JSON -->
#     <textarea id="jsonInput" rows="10" cols="50" placeholder="請在此處貼上JSON數據"></textarea>
#     <br>
#     <button onclick="parseJson()">解析</button>

#     <h2>解析結果</h2>
#     <pre id="output"></pre>

#     <script>
#         function parseJson() {
#             // 獲取輸入框中的JSON文本
#             const jsonText = document.getElementById('jsonInput').value;

#             try {
#                 // 解析JSON文本
#                 const reData = JSON.parse(jsonText);
#                 const items = reData["items"];
#                 const output = [];

#                 // 遍歷每個物品並提取數據
#                 for (const i of items) {
#                     const temp = {
#                         "name": i["typeLine"],
#                         "values": parseInt(i["properties"][0]["values"][0][0].split("/")[0])
#                     };
#                     output.push(temp);
#                 }

#                 // 將結果顯示在頁面上
#                 document.getElementById('output').textContent = JSON.stringify(output, null, 2);

#             } catch (error) {
#                 document.getElementById('output').textContent = "解析錯誤：" + error.message;
#             }
#         }
#     </script>
# </body>
# </html>
