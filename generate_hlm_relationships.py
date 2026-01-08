#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《红楼梦》人物关系图生成器"""

import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "STHeiti"]
plt.rcParams["axes.unicode_minus"] = False

# 节点和颜色
nodes_data = {
    # 贾府核心
    "贾母": [0, 3, "#4ECDC4", 800, "main"],
    "贾赦": [-1, 2.5, "#4ECDC4", 700, "main"],
    "贾政": [1, 2.5, "#4ECDC4", 800, "main"],
    "贾宝玉": [0, 1, "#4ECDC4", 1000, "main"],
    "贾珠": [-1, 0.5, "#4ECDC4", 700, "main"],
    "贾琏": [-0.5, 0, "#4ECDC4", 700, "main"],
    "王熙凤": [0.5, 1, "#45B7D1", 700, "female"],
    "李纨": [-1.5, 0, "#4ECDC4", 500, "female"],
    "巧姐": [-2, 0, "#4ECDC4", 500, "female"],
    "贾探春": [0.5, -0.5, "#4ECDC4", 500, "female"],
    "贾环": [1, -0.5, "#4ECDC4", 700, "main"],
    "贾元春": [-1, -1, "#4ECDC4", 500, "female"],
    # 其他家族
    "薛宝钗": [1.5, 0.5, "#96CEB4", 700, "female"],
    "林黛玉": [0.5, -0.5, "#FF9F43", 700, "female"],
    "史湘云": [0, -0.5, "#F7DC6F", 600, "female"],
}


# 绘制函数
def draw_arrow(ax, x1, y1, x2, y2, color="black"):
    dx = x2 - x1
    dy = y2 - y1
    length = (dx**2 + dy**2) ** 0.5
    if length < 0.01:
        return
    nx = dx / length
    ny = dy / length
    ax.arrow(
        x1,
        y1,
        dx,
        dy,
        head_width=0.15,
        head_length=0.3,
        fc=color,
        ec=color,
        alpha=0.8,
        width=1.5,
    )


def draw_line(ax, x1, y1, x2, y2, color, linestyle="-"):
    ax.plot(
        [x1, x2], [y1, y2], color=color, linestyle=linestyle, linewidth=2, alpha=0.7
    )


# 创建图形
fig = plt.figure(figsize=(28, 20))

# 子图1: 贾府核心人物关系
ax1 = fig.add_subplot(2, 2, 1)

# 绘制连接
draw_line(ax1, 0, 3, 1, 2.5, "gray")
draw_line(ax1, 1, 2.5, 0, 3, "gray")
draw_line(ax1, 1, 2.5, -1, 0.5, "gray")
draw_line(ax1, -1, 0.5, -0.5, 0, "gray")
draw_line(ax1, 0.5, 0, -2, 0, "gray")
draw_line(ax1, 0.5, 0, -2, 0, "gray")
draw_line(ax1, 0, 0, 2.5, 0.5, "gray")
draw_line(ax1, 1, 0, 2.5, 0.5, "gray")
draw_line(ax1, 1, 0, -2, 0, "gray")
draw_line(ax1, 1, 0, -2, 0, "gray")
draw_line(ax1, 0.5, 1.5, 0, "gray")
draw_line(ax1, -1, 2.5, 0, 0.5, "green")
draw_line(ax1, -1, 2.5, 0, 0.5, "green")
draw_line(ax1, 0.5, 0, 0, 0, "green")
draw_line(ax1, 0.5, 1, 2.5, 0, "green")

# 绘制箭头
draw_arrow(ax1, 1, 2.5, 0, 3, "black")
draw_arrow(ax1, 0.5, 1.5, 0, 0.5, "black")
draw_arrow(ax1, 1, 2.5, -1, 0.5, "black")
draw_arrow(ax1, 0.5, 0.0 - 2, 0, "black")
draw_arrow(ax1, 0.5, 0, -0.5, 0, "black")
draw_arrow(ax1, 0.5, 0, 1.5, 0, 5, "black")
draw_arrow(ax1, 0.5, 1.5, 1.5, 1.5, "black")
draw_arrow(ax1, 0.5, 1.5, 1.5, 1, 0.5, "black")
draw_arrow(ax1, 0.5, 1.5, 0, 0.5, "black")
draw_arrow(ax1, 0.5, 1.5, 0, 0.5, "black")
draw_arrow(ax1, 1, 1.5, 2, 0.5, "black")
draw_arrow(ax1, -1, 2.5, 0, 0.5, "black")
draw_arrow(ax1, -1, 2.5, 0, 0, "green")

# 绘制节点
for name, (x, y, color, size, ntype) in [
    (name, *nodes_data[name]) for name in nodes_data.keys()
]:
    plt.scatter(x, y, s=size, c=color, alpha=0.9, edgecolors="black", linewidths=2)

# 添加节点标签
for name in nodes_data.keys():
    x, y = nodes_data[name][0], nodes_data[name][1]
    color = nodes_data[name][2]
    size = nodes_data[name][3]
    ntype = nodes_data[name][4]
    font_size = 14 if ntype == "main" else 11
    font_weight = "bold" if ntype == "main" else "normal"
    plt.text(
        x,
        y + 0.12,
        name,
        fontsize=font_size,
        fontweight=font_weight,
        ha="center",
        va="center",
        fontproperties={"family": "SimHei"},
    )

ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-1.5, 3.5)
ax1.set_title("荣国府核心人物关系", fontsize=16, fontweight="bold", pad=20)
ax1.axis("off")

# 添加说明
desc1 = "说明:\n- 实线: 血缘/婚姻关系\n- 虚线: 情感/特殊关系\n- 圈大: 主要人物\n- 圈中: 女性人物"
ax1.text(
    -2.3,
    -1.3,
    desc1,
    fontsize=9,
    va="top",
    ha="left",
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.3),
)

# 子图2: 贾宝玉情感与权力网络
ax2 = fig.add_subplot(2, 2, 2)

# 绘制连接
draw_line(ax2, 0, 1, 1.5, -0.5, "red", "--")
draw_line(ax2, 1, 1.5, 0.5, 0.5, "green")
draw_line(ax2, 0.5, 0.5, 0.5, -1, "#45B7D1", "--")
draw_line(ax2, 1.5, 0.5, 1.5, 0, "#F7DC6F", "--")
draw_line(ax2, 0.5, 0.5, 0.5, -1.5, "#96CEB4", "--")

# 绘制箭头
draw_arrow(ax2, 0, 0.5, 0, 1.5, "red")
draw_arrow(ax2, 0.5, 1.5, 1.5, 1.5, "green")
draw_arrow(ax2, 0.5, 0.5, 0, 1.5, "blue")

# 绘制贾宝玉
plt.scatter(
    0, 1, s=1500, c="#4ECDC4", alpha=0.9, edgecolors="black", linewidths=3, ax=ax2
)
plt.text(
    0,
    1,
    "贾宝玉\n(中心)",
    fontsize=16,
    fontweight="bold",
    ha="center",
    va="center",
    ax=ax2,
)

# 绘制周围人物
bx_data = [
    ("林黛玉", 0, 1.5, "#FF9F43"),
    ("薛宝钗", 1.5, 0.5, "#96CEB4"),
    ("王熙凤", 0.5, -1, "#45B7D1"),
    ("史湘云", -1.5, 0.5, "#F7DC6F"),
]

for name, x, y, color in bx_data:
    plt.scatter(
        x, y, s=800, c=color, alpha=0.9, edgecolors="black", linewidths=2, ax=ax2
    )
    plt.text(
        x,
        y - 0.12,
        name,
        fontsize=12,
        fontweight="normal",
        ha="center",
        va="center",
        ax=ax2,
    )

# 添加关系说明
desc2 = "关系类型:\n- 红色虚线: 木石前盟(林黛玉)\n- 绿色实线: 后娶(薛宝钗)\n- 蓝色虚线: 权力影响(王熙凤)\n- 蓝色虚线: 表兄妹(史湘云)"
ax2.text(
    -1.8,
    -1.5,
    desc2,
    fontsize=9,
    va="top",
    ha="left",
    bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.3),
)

ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-2, 2)
ax2.set_title("贾宝玉情感与权力网络", fontsize=16, fontweight="bold", pad=20)
ax2.axis("off")

# 子图3: 四大家族联姻网络
ax3 = fig.add_subplot(2, 2, 3)

# 家族位置
family_positions = {
    "贾家": (-1.5, 1),
    "史家": (-0.5, 1),
    "王家": (0.5, 1),
    "薛家": (-0.5, 0.5),
    "林家": (0.5, 0.5),
}

family_colors = {
    "贾家": "#FF6B6B",
    "史家": "#F7DC6F",
    "王家": "#45B7D1",
    "薛家": "#96CEB4",
    "林家": "#FF9F43",
}

# 联姻关系
marriage_lines = [
    ("贾家", "史家"),
    ("贾家", "王家"),
    ("贾家", "薛家"),
    ("史家", "贾家"),
    ("王家", "贾家"),
    ("薛家", "贾家"),
]

# 绘制联姻线
for fam1, fam2 in marriage_lines:
    x1, y1 = family_positions[fam1]
    x2, y2 = family_positions[fam2]
    draw_line(ax3, x1, y1, x2, y2, "gray")

# 绘制家族节点
for family, (x, y) in family_positions.items():
    plt.scatter(
        x,
        y,
        s=2000,
        c=family_colors[family],
        alpha=0.9,
        edgecolors="black",
        linewidths=3,
        ax=ax3,
    )
    plt.text(
        x,
        y + 0.2,
        family,
        fontsize=15,
        fontweight="bold",
        ha="center",
        va="center",
        ax=ax3,
    )

# 添加说明
desc3 = "护官符:\n贾不假，白玉为堂金作马。\n阿房宫，三百里，住不下金陵一个史。\n东海缺少白玉床，龙王来请金陵王。\n丰年好大雪，珍珠如土金如铁。\n\n核心原则:\n连络有亲，一损皆损，一荣皆荣。"
ax3.text(
    -2,
    -1.8,
    desc3,
    fontsize=10,
    va="top",
    ha="left",
    bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.3),
)

ax3.set_xlim(-2.2, 1.5)
ax3.set_ylim(-2, 2)
ax3.set_title("四大家族联姻网络(护官符)", fontsize=16, fontweight="bold", pad=20)
ax3.axis("off")

fig.suptitle("《红楼梦》人物关系结构图", fontsize=22, fontweight="bold", y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.97])

output_file = "/Users/ibepo/Documents/GitHub/doc2/红楼梦人物关系结构图.pdf"
plt.savefig(output_file, format="pdf", dpi=300, bbox_inches="tight")

print(f"✅ PDF已成功生成: {output_file}")
print(f"📊 包含3个子图:")
print(f"   1. 荣国府核心人物关系")
print(f"   2. 贾宝玉情感与权力网络")
print(f"   3. 四大家族联姻网络(护官符)")
