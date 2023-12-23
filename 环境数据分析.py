import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageTk



# 省份和城市的数据，可以根据需要添加或修改
province_cities = {
    '北京市': ['北京'],
    '天津市': ['天津'],
    '河北省': ['石家庄', '唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水'],
    '山西省': ['太原', '大同', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '忻州', '临汾', '吕梁'],
    '内蒙古自治区': ['呼和浩特', '包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布','兴安盟', '锡林郭勒盟', '阿拉善盟'],
    '辽宁省': ['沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛'],
    '吉林省': ['长春', '吉林市', '四平', '辽源', '通化', '白山', '松原', '白城', '延边朝鲜族自治州'],
    '黑龙江省': ['哈尔滨', '齐齐哈尔', '牡丹江', '佳木斯', '大庆', '伊春', '鸡西', '鹤岗', '双鸭山', '七台河', '绥化', '黑河', '大兴安岭地区'],
    '上海市': ['上海'],
    '江苏省': ['南京', '苏州', '无锡', '常州', '镇江', '南通', '泰州', '扬州', '盐城', '连云港', '淮安', '徐州', '宿迁'],
    '浙江省': ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水'],
    '安徽省': ['合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '六安','亳州', '池州', '宣城'],
    '福建省': ['福州', '厦门', '莆田', '三明', '泉州', '漳州', '南平', '龙岩', '宁德'],
    '江西省': ['南昌', '赣州', '宜春', '吉安', '上饶', '抚州', '九江', '景德镇', '萍乡', '新余', '鹰潭'],
    '山东省': ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂','德州', '聊城', '滨州', '菏泽'],
    '河南省': ['郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡','南阳', '商丘', '信阳', '周口', '驻马店'],
    '湖北省': ['武汉', '黄石', '十堰', '宜昌', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州','恩施土家族苗族自治州', '仙桃', '潜江', '天门', '神农架林区'],
    '湖南省': ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底','湘西土家族苗族自治州'],
    '广东省': ['广州', '深圳', '珠海', '汕头', '韶关', '佛山', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾','河源', '阳江', '清远', '东莞', '中山', '潮州', '揭阳', '云浮'],
    '广西壮族自治区': ['南宁', '柳州', '桂林', '梧州', '北海', '防城港', '钦州', '贵港', '玉林', '百色', '贺州', '河池','来宾', '崇左'],
    '海南省': ['海口', '三亚', '三沙', '儋州', '五指山', '琼海', '文昌', '万宁', '东方', '定安县', '屯昌县', '澄迈县','临高县', '白沙黎族自治县', '昌江黎族自治县', '乐东黎族自治县', '陵水黎族自治县', '保亭黎族苗族自治县','琼中黎族苗族自治县'],
    '重庆市': ['重庆'],
    '四川省': ['成都', '自贡', '攀枝花', '泸州', '德阳', '绵阳', '广元', '遂宁', '内江', '乐山', '南充', '眉山', '宜宾','广安', '达州', '雅安', '巴中', '资阳', '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州'],
    '贵州省': ['贵阳', '六盘水', '遵义', '安顺', '毕节', '铜仁', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州','黔南布依族苗族自治州'],
    '云南省': ['昆明', '曲靖', '玉溪', '保山', '昭通', '丽江', '普洱', '临沧', '楚雄彝族自治州', '红河哈尼族彝族自治州','文山壮族苗族自治州', '西双版纳傣族自治州', '大理白族自治州', '德宏傣族景颇族自治州', '怒江傈僳族自治州','迪庆藏族自治州'],
    '西藏自治区': ['拉萨', '日喀则', '昌都', '林芝', '山南', '那曲', '阿里'],
    '陕西省': ['西安', '铜川', '宝鸡', '咸阳', '渭南', '延安', '汉中', '榆林', '安康', '商洛'],
    '甘肃省': ['兰州', '嘉峪关', '金昌', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南','临夏回族自治州', '甘南藏族自治州'],
    '青海省': ['西宁', '海东', '海北藏族自治州', '黄南藏族自治州', '海南藏族自治州', '果洛藏族自治州', '玉树藏族自治州','海西蒙古族藏族自治州'],
    '宁夏回族自治区': ['银川', '石嘴山', '吴忠', '固原', '中卫'],
    '新疆维吾尔自治区': ['乌鲁木齐', '克拉玛依', '吐鲁番', '哈密', '昌吉回族自治州', '博尔塔拉蒙古自治州','巴音郭楞蒙古自治州', '阿克苏地区', '克孜勒苏柯尔克孜自治州', '喀什地区', '和田地区','伊犁哈萨克自治州', '塔城地区', '阿勒泰地区']
}

def on_province_select(event):
    selected_province = province_combobox.get()
    cities = province_cities.get(selected_province, [])
    city_combobox['values'] = cities

def on_city_select(selected_city):
    selected_city = city_combobox.get()
    return selected_city


#调用和风天气API获取实时空气质量
def weatherapi():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei或你系统中存在的合适字体
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    api_key = "6ae348c85af540c79479f9e5d4f8e130"  # 和风天气 API 密钥
    global city
    city = city_combobox.get()                                         # 查询天气的城市
    #城市LocationID搜索
    global locationid, aircondition
    #geoapi 获取城市LocationID
    geoapi_url = "https://geoapi.qweather.com/v2/city/lookup"
    geoapi_params = {
        "location": city,
        "key": api_key,
    }

    location_response = requests.get(geoapi_url, params=geoapi_params)
    if location_response.status_code == 200:
        locationid_data = location_response.json()
        locationid = locationid_data['location'][0]['id']


    hefeng_url = "https://devapi.qweather.com/v7/air/now"
    hefeng_params = {
        "location": locationid,
        "key": api_key,
    }

    response = requests.get(hefeng_url, params=hefeng_params)
    if response.status_code == 200:
        weather_data = response.json()
        aircondition = f"{city}当前空气质量如下: \n 空气质量指数: {weather_data['now']['aqi']} \n 空气质量指数级别: {weather_data['now']['category']} \n 空气质量的主要污染物:{weather_data['now']['primary']} \n PM2.5指数: {weather_data['now']['pm2p5']} \n PM10指数:{weather_data['now']['pm2p5']} \n 二氧化氮指数:{weather_data['now']['no2']} \n 二氧化硫指数:{weather_data['now']['so2']} \n 一氧化碳指数:{weather_data['now']['co']} \n 臭氧指数:{weather_data['now']['o3']}"
        weather_text.insert(tk.END, aircondition)
    else:
        weather_text.delete(1.0, tk.END)  # 清空结果框
        weather_text.insert(tk.END, "和风API调用失败，请检查您的网络连接和API密钥是否正确。")

    return aircondition

#将空气质量传入chatgptAPI
def chatgptapi():
    weather_text.configure(state="normal")
    jianyi_text.configure(state="normal")
    try:
        with open("API.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                api_endpoint = lines[0].strip()
                api_key = lines[1].strip()
    except FileNotFoundError:
        jianyi_text.delete(1.0, tk.END)
        jianyi_text.insert(tk.END, "未找到API设置文件。请先设置API。")
        return

    aircondition = weatherapi()

    # 你的空气质量信息
    inputs = f"请帮我根据我给的空气质量做出分析并给出建议，{aircondition}"

    # 调用 ChatGPT API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # 分割文本为较小的块（比如每次发送500个字符）
    chunk_size = 500
    chunks = [inputs[i:i+chunk_size] for i in range(0, len(inputs), chunk_size)]

    generated_text = ""

    # 逐个发送每个块并处理响应
    for chunk in chunks:
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': chunk}]
        }
        response = requests.post(api_endpoint, json=data, headers=headers)

        # 处理每个块的API返回内容
        if response.status_code == 200:
            content = response.json()
            generated_text += content['choices'][0]['message']['content']
        else:
            jianyi_text.delete(1.0, tk.END)  # 清空结果框
            jianyi_text.insert(tk.END, "ChatGPT API调用失败，请检查网络连接和API密钥。")
            return

    # 在循环结束后插入最终生成的文本
    jianyi_text.delete(1.0, tk.END)  # 清空结果框
    jianyi_text.insert(tk.END, generated_text)
    weather_text.configure(state="disabled")
    jianyi_text.configure(state="disabled")


def open_api_window():
    api_window = tk.Toplevel(root)
    api_window.title("API设置")
    api_window.iconbitmap("./icon.ico")
    # 获取屏幕尺寸和窗口尺寸
    api_window_width = 450
    api_window_height = 180
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口居中时左上角的坐标
    x = (screen_width - api_window_width) // 2
    y = (screen_height - api_window_height) // 2

    # 设置窗口尺寸和放置位置
    api_window.geometry(f'{api_window_width}x{api_window_height}+{x}+{y}')

    entry1 = tk.Entry(api_window, width=api_window_width)
    entry2 = tk.Entry(api_window, width=api_window_width)

    # 尝试从文件中读取内容
    try:
        with open("API.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                entry1.insert(0, lines[0].strip())
                entry2.insert(0, lines[1].strip())
    except FileNotFoundError:
        pass

    def save_and_close():
        # 保存输入框内容到文件
        with open("API.txt", "w") as file:
            file.write(entry1.get() + "\n")
            file.write(entry2.get() + "\n")
        api_window.destroy()

    # 布局输入框和保存按钮
    jiekou = tk.Label(api_window, text="API接口:")
    jiekou.pack()

    entry1.pack()

    space = tk.Label(api_window, text="")
    space.pack()

    key = tk.Label(api_window, text="KEY:")
    key.pack()

    entry2.pack()

    space1 = tk.Label(api_window, text="")
    space1.pack()

    save_button = tk.Button(api_window, text="保存", command=save_and_close)
    save_button.pack()

def show_line_chart():
    # 创建新的窗口
    chart_window = tk.Toplevel(root)
    chart_window.title("五天空气质量预报折线图")
    chart_window.iconbitmap("./icon.ico")


    # 获取空气质量数据

    hefeng_forecast_url = "https://devapi.qweather.com/v7/air/5d"  # 获取五天空气质量预报的API
    api_key = "6ae348c85af540c79479f9e5d4f8e130"  # 和风天气 API 密钥
    hefeng_forecast_params = {
        "location": locationid,
        "key": api_key,
    }

    forecast_response = requests.get(hefeng_forecast_url, params=hefeng_forecast_params)
    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()
        air_quality_forecast = forecast_data['daily']

        # 提取日期和空气质量指数
        dates = [day['fxDate'] for day in air_quality_forecast]
        air_quality_index = [day['aqi'] for day in air_quality_forecast]

        # 绘制折线图
        plt.figure(figsize=(8, 5))
        plt.plot(dates, air_quality_index, marker='o', linestyle='-', color='b')
        plt.title(f'{city}五天空气质量预报')
        plt.xlabel('日期')
        plt.ylabel('空气质量指数')
        plt.xticks(rotation=45)
        plt.tight_layout()

        image_file = f"{city}五天空气质量预报.png"
        # 保存折线图为图片文件
        plt.savefig(image_file)
        plt.close()

        # 打开并显示折线图
        image = Image.open(image_file)
        image = ImageTk.PhotoImage(image)

        # 在新窗口中显示折线图到Label部件
        image_label = tk.Label(chart_window, image=image)
        image_label.image = image
        image_label.pack()

        # 生成折线图
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei或你系统中存在的合适字体
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        # 获取折线图尺寸
        image = Image.open(image_file)
        width, height = image.size

        # 设置新窗口大小，稍大于折线图的尺寸
        chart_window.geometry(f"{width + 20}x{height + 20}")  # 20像素的额外空间




# 创建主窗口
root = tk.Tk()
root.title("环境数据分析")
style = ttk.Style("litera")

# 设置图标
root.iconbitmap("./icon.ico")


# 创建选项菜单
menubar = tk.Menu(root)
menubar.add_command(label="API设置", command=open_api_window)
root.config(menu=menubar)


# 创建省份下拉框
province_label = tk.Label(root, text="选择省份:")
province_label.pack()

province_combobox = ttk.Combobox(root, values=list(province_cities.keys()))
province_combobox.pack()
province_combobox.bind("<<ComboboxSelected>>", on_province_select)

# 添加空间调整下拉框之间的距离
space = tk.Label(root, text="")
space.pack()

# 创建城市下拉框
city_label = tk.Label(root, text="选择城市:")
city_label.pack()

city_combobox = ttk.Combobox(root, values=[])
city_combobox.pack()
city_combobox.bind("<<ComboboxSelected>>", on_city_select)

# 添加空间调整下拉框和文本框之间的距离
space2 = tk.Label(root, text="")
space2.pack()


#创建按钮
custom_padding = (80, 20, 80, 20)
button = ttk.Button(root, text="查询", command=chatgptapi, bootstyle=SUCCESS, padding=custom_padding)
button.size = (10,100)
button.pack(padx=10, pady=10)

custom_padding = (80, 20, 80, 20)
button = ttk.Button(root, text="查看折线图", command=show_line_chart, padding=custom_padding)
button.size = (10,100)
button.pack(padx=10, pady=10)


space3 = tk.Label(root, text="")
space3.pack()

#创建天气状况
weather_label = tk.Label(root, text=f"天气状况:")
weather_label.pack()

weather_text = ttk.Text(root, height=5, width=50, state="normal")
weather_text.pack()


space4 = tk.Label(root, text="")
space4.pack()

# 创建建议文本框
jianyi_label = tk.Label(root, text="分析&建议:")
jianyi_label.pack()

jianyi_text = tk.Text(root, height=13, width=50, state="normal")
jianyi_text.pack()

# 获取屏幕尺寸和窗口尺寸
window_width = 450
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口居中时左上角的坐标
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口尺寸和放置位置
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

root.mainloop()