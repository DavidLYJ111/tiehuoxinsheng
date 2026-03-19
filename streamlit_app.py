from pathlib import Path

import streamlit as st


# -----------------------------
# 基础配置
# -----------------------------
st.set_page_config(
    page_title="铁火新生",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
IMG_DIR = BASE_DIR / "static" / "images"


def img_path(filename: str) -> str:
    return str(IMG_DIR / filename)


def section_title(title: str, subtitle: str = "") -> None:
    st.markdown(f"""
    <div style="margin-top: 10px; margin-bottom: 20px;">
        <h2 style="color:#8B1E1E; margin-bottom: 6px;">{title}</h2>
        <p style="color:#6B6B6B; margin-top: 0;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def card(title: str, text: str) -> None:
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border-radius:18px;
            padding:22px 20px;
            box-shadow:0 8px 24px rgba(0,0,0,0.06);
            border:1px solid rgba(139,30,30,0.08);
            min-height:180px;">
            <h4 style="color:#8B1E1E; margin-top:0;">{title}</h4>
            <p style="color:#5F5954; line-height:1.8;">{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# 自定义样式
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: #F7F3EE;
    }
    .main-title {
        font-size: 54px;
        font-weight: 800;
        color: #8B1E1E;
        margin-bottom: 8px;
    }
    .sub-title {
        font-size: 24px;
        font-weight: 700;
        color: #C9A46C;
        margin-bottom: 16px;
    }
    .desc {
        color: #5F5954;
        font-size: 17px;
        line-height: 1.9;
    }
    .hero-box {
        background: linear-gradient(135deg, #F4EEE7 0%, #F7F3EE 100%);
        padding: 26px;
        border-radius: 24px;
        border: 1px solid rgba(139,30,30,0.08);
    }
    .pill-wrap {
        display:flex;
        gap:12px;
        flex-wrap:wrap;
        margin-top:18px;
    }
    .pill {
        background:#FFFFFF;
        border-radius:16px;
        padding:12px 16px;
        border:1px solid rgba(139,30,30,0.08);
        box-shadow:0 8px 20px rgba(0,0,0,0.04);
        min-width:130px;
    }
    .pill strong {
        display:block;
        color:#8B1E1E;
        font-size:20px;
    }
    .pill span {
        color:#6B6B6B;
        font-size:13px;
    }
    .footer-box {
        text-align:center;
        color:#6B6B6B;
        padding:18px 0 8px 0;
        font-size:14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 侧边栏导航
# -----------------------------
with st.sidebar:
    logo = IMG_DIR / "logo.png"
    if logo.exists():
        st.image(str(logo), width=90)

    st.markdown("## 铁火新生")
    st.markdown("合肥工业大学 · 三创赛项目")

    page = st.radio(
        "页面导航",
        ["首页", "项目背景", "产品体系", "技术创新", "数字平台"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.caption("非遗活化 · 材料创新 · 数字赋能")


# -----------------------------
# 首页
# -----------------------------
if page == "首页":
    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        st.markdown('<div class="hero-box">', unsafe_allow_html=True)
        st.markdown('<div style="color:#8B1E1E;background:rgba(139,30,30,0.08);display:inline-block;padding:6px 14px;border-radius:999px;font-size:14px;">国家级非遗活化项目构想</div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:10px;color:#6B6B6B;font-size:14px;">合肥工业大学 · 三创赛项目</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">铁火新生</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">让非遗成为触手可及的生活美学</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="desc">以材料创新、产品年轻化与数字平台赋能为核心，推动芜湖铁画从传统工艺品走向生活化、可传播、可持续的当代非遗品牌。</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="pill-wrap">
                <div class="pill"><strong>3 大</strong><span>核心业务体系</span></div>
                <div class="pill"><strong>3 层</strong><span>产品矩阵覆盖</span></div>
                <div class="pill"><strong>1 站式</strong><span>数字云平台原型</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.image(img_path("home-hero.png"), use_container_width=True)

    st.divider()

    section_title("核心价值", "从工艺传承到商业转化，构建非遗创新的完整路径")
    c1, c2, c3 = st.columns(3)
    with c1:
        card("材料创新", "以轻量化、耐久化与环保导向优化传统铁画材料体系，增强产品落地能力。")
    with c2:
        card("产品年轻化", "以文创、家居、礼赠和收藏等多元场景切入，拓宽铁画的当代生活应用。")
    with c3:
        card("数字平台赋能", "通过“铁火云社”连接展示、教学、购买、传播与社群互动，增强用户黏性。")

    st.divider()

    section_title("三大产品系列", "覆盖年轻消费、生活美学与高端收藏三类核心场景")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.image(img_path("xinsheng.png"), use_container_width=True)
        st.markdown("### 轻语·新生系列")
        st.write("聚焦轻量化、年轻化与入门级文创体验，适合礼赠、校园与文旅消费。")
    with p2:
        st.image(img_path("wanxiang.png"), use_container_width=True)
        st.markdown("### 万象·生活系列")
        st.write("以家居、办公与实用美学为主，让非遗不止于收藏，也能进入日常生活。")
    with p3:
        st.image(img_path("zhencang.png"), use_container_width=True)
        st.markdown("### 永恒·珍藏系列")
        st.write("强调定制、纪念与收藏价值，面向高端礼赠与文化审美型消费群体。")

    st.divider()

    section_title("项目亮点展示", "以产品、传播与场景化设计共同构建品牌触达路径")
    h1, h2, h3 = st.columns(3)
    with h1:
        st.image(img_path("blindbox.png"), use_container_width=True)
        st.markdown("### IP盲盒文创")
        st.write("以“名山铁画”等形式提升产品趣味性、收藏性与年轻化传播能力。")
    with h2:
        st.image(img_path("campus-event.png"), use_container_width=True)
        st.markdown("### 校园活动推广")
        st.write("通过宣讲、体验和互动展示增强年轻人对非遗的感知、参与和认同。")
    with h3:
        st.image(img_path("gift-box.png"), use_container_width=True)
        st.markdown("### 场景化礼赠设计")
        st.write("赋予铁画更强的节庆、文旅、纪念与商务礼赠价值。")

    st.divider()

    section_title("品牌服务矩阵")
    s1, s2 = st.columns([1, 1], gap="large")
    with s1:
        st.write(
            "除产品开发外，项目还可延展为品牌视觉、传播内容、文旅礼赠、教学体验、活动策划等综合服务体系，形成更强的商业闭环。"
        )
        st.write(
            "这部分特别适合比赛答辩时说明：我们做的不是单一产品，而是一套非遗品牌化解决方案。"
        )
    with s2:
        st.image(img_path("pinpaifuwujuzheng.png"), use_container_width=True)

    st.divider()

    section_title("宣传与包装延展", "从包装、宣传册到海报，进一步完善品牌视觉传播体系")
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        st.image(img_path("chanpinbaozhuang.png"), use_container_width=True)
        st.caption("产品包装设计")
    with a2:
        st.image(img_path("xuanchuance.png"), use_container_width=True)
        st.caption("品牌宣传册")
    with a3:
        st.image(img_path("xuanchuanhaibao.png"), use_container_width=True)
        st.caption("线下传播海报")
    with a4:
        st.image(img_path("lihe2.png"), use_container_width=True)
        st.caption("礼盒方案延展")

    st.divider()

    section_title("数字平台原型")
    d1, d2 = st.columns([1, 1], gap="large")
    with d1:
        st.write("平台集非遗教学、在线展示、商城交易、互动传播于一体，支撑“产品—用户—内容—社群”的持续连接。")
        st.write("通过“铁火云社”平台，可承载课程体验、作品展示、产品交易、用户互动与品牌内容传播等多重功能。")
    with d2:
        st.image(img_path("platform-ui.png"), use_container_width=True)

    st.divider()

    section_title("平台传播能力")
    b1, b2, b3 = st.columns(3)
    with b1:
        st.image(img_path("ar-demo.png"), use_container_width=True)
        st.markdown("### AR互动体验")
        st.write("增强产品内容表达，让非遗传播更具沉浸感与参与感。")
    with b2:
        st.image(img_path("live-stream.png"), use_container_width=True)
        st.markdown("### 直播传播")
        st.write("拓宽展示和销售渠道，增强实时互动能力与传播转化效率。")
    with b3:
        st.image(img_path("brand-video.png"), use_container_width=True)
        st.markdown("### 品牌内容输出")
        st.write("通过视觉内容与短视频讲好铁画故事，形成持续的品牌记忆点。")

    st.divider()

    section_title("专家背书与指导支持")
    e1, e2 = st.columns([1, 1], gap="large")
    with e1:
        st.write("专家、教师与跨学科指导资源，能够提升项目在材料、工艺、品牌、商业策划与非遗传播层面的专业性和可信度。")
    with e2:
        st.image(img_path("professor(zhuanjia).png"), use_container_width=True)


# -----------------------------
# 项目背景
# -----------------------------
elif page == "项目背景":
    section_title("项目背景", "从市场痛点出发，回应非遗铁画在当代传播与应用中的现实问题")

    c1, c2, c3 = st.columns(3)
    with c1:
        card("传统材料局限", "传统铁画存在重量较大、易锈蚀、运输与日常使用不便等问题。")
    with c2:
        card("产品场景较单一", "主要集中在观赏和收藏，生活化、年轻化应用场景相对不足。")
    with c3:
        card("传播方式偏传统", "与年轻消费群体之间缺乏持续互动，线上内容生态有待完善。")

    st.divider()

    l1, l2 = st.columns([1, 1], gap="large")
    with l1:
        st.markdown("### 调研支撑")
        st.write("项目通过市场问卷与用户调研，梳理出年轻消费群体对非遗文创在轻量化、美学表达、数字互动与购买便捷性方面的需求。")
        st.write("这页适合答辩时说明：我们不是凭空想象，而是基于真实市场与用户反馈做产品设计。")
    with l2:
        st.image(img_path("survey-report.png"), use_container_width=True)

    st.divider()

    section_title("我们的解决方案")
    s1, s2, s3 = st.columns(3)
    with s1:
        card("创新材料", "改善传统材质短板，提高产品耐久性与使用友好度。")
    with s2:
        card("分层产品矩阵", "覆盖年轻消费、日常生活、礼赠定制与高端收藏等不同市场。")
    with s3:
        card("数字化平台", "打通展示、传播、学习、购买和社群互动等多维触点。")


# -----------------------------
# 产品体系
# -----------------------------
elif page == "产品体系":
    section_title("产品体系", "围绕不同消费层级与使用场景，构建三大产品矩阵")

    st.image(img_path("product-series.png"), use_container_width=True)
    st.caption("产品矩阵总览")

    st.divider()

    p1, p2, p3 = st.columns(3)
    with p1:
        st.image(img_path("xinsheng.png"), use_container_width=True)
        st.markdown("### 轻语·新生系列")
        st.write("主打轻巧、便携、时尚和年轻表达，适合文创礼品、校园市场与文旅消费。")
    with p2:
        st.image(img_path("wanxiang.png"), use_container_width=True)
        st.markdown("### 万象·生活系列")
        st.write("将非遗审美融入居家与办公日常，让铁画从“看”走向“用”。")
    with p3:
        st.image(img_path("zhencang.png"), use_container_width=True)
        st.markdown("### 永恒·珍藏系列")
        st.write("面向高端礼赠、纪念定制与收藏场景，突出工艺价值与文化价值。")

    st.divider()

    g1, g2 = st.columns([1, 1], gap="large")
    with g1:
        st.markdown("### 礼盒与包装方案")
        st.write("在产品本体之外，项目还强调包装设计、礼盒场景和品牌视觉延展，进一步增强产品的纪念意义、礼赠属性和市场识别度。")
    with g2:
        st.image(img_path("chanpinbaozhuang.png"), use_container_width=True)

    st.divider()

    x1, x2, x3 = st.columns(3)
    with x1:
        st.image(img_path("gift-box.png"), use_container_width=True)
        st.caption("纪念礼盒方案")
    with x2:
        st.image(img_path("lihe2.png"), use_container_width=True)
        st.caption("礼盒延展设计")
    with x3:
        st.image(img_path("xinsheng.png"), use_container_width=True)
        st.caption("系列化开发思路")


# -----------------------------
# 技术创新
# -----------------------------
elif page == "技术创新":
    section_title("技术创新", "从材料到工艺，再到业务体系，形成可持续的非遗创新路径")

    t1, t2 = st.columns([1, 1], gap="large")
    with t1:
        st.markdown("### 材料工艺创新")
        st.write("项目围绕轻量化、耐久化和可持续方向，探索再生金属材料、防锈处理与新型工艺路径，提高铁画产品在现代消费场景中的适配能力。")
    with t2:
        st.image(img_path("material-process.png"), use_container_width=True)

    st.divider()

    d1, d2 = st.columns([1, 1], gap="large")
    with d1:
        st.markdown("### 低碳钢基材优化")
        st.write("通过对基材选择和处理方式进行优化，提升产品强度、稳定性与后续工艺适配能力，为铁画从传统工艺品向现代文创和生活产品转化提供基础支撑。")
    with d2:
        st.image(img_path("ditangangjicai.png"), use_container_width=True)

    st.divider()

    r1, r2 = st.columns([1, 1], gap="large")
    with r1:
        st.markdown("### 技术路线")
        st.write("从需求调研、产品方向设计、材料与工艺优化，到数字平台传播和市场转化，构建起完整的项目落地路径。")
    with r2:
        st.image(img_path("tech-route.png"), use_container_width=True)

    st.divider()

    y1, y2 = st.columns([1, 1], gap="large")
    with y1:
        st.markdown("### 业务系统支撑")
        st.write("通过技术创新、品牌运营与数字平台三者协同，推动铁画产品从单一工艺品向系统化品牌项目升级。")
    with y2:
        st.image(img_path("business-system.png"), use_container_width=True)


# -----------------------------
# 数字平台
# -----------------------------
elif page == "数字平台":
    section_title("数字平台", "构建集展示、教学、商城、社群互动于一体的“铁火云社”平台原型")

    p1, p2 = st.columns([1, 1], gap="large")
    with p1:
        st.markdown("### 平台首页原型")
        st.write("平台承载品牌展示、非遗科普、产品购买、互动活动与用户共创等功能，是连接项目内容与用户触达的重要入口。")
    with p2:
        st.image(img_path("platform-ui.png"), use_container_width=True)

    st.divider()

    h1, h2 = st.columns([1, 1], gap="large")
    with h1:
        st.markdown("### 铁火云社数字平台")
        st.write("除基础展示与商城外，平台还可延展到创作交流、用户互动、非遗学习、活动组织与社群协作等层面，进一步增强项目的社区属性与持续运营能力。")
    with h2:
        st.image(img_path("tiehuoyunsheshuzipingtai.png"), use_container_width=True)

    st.divider()

    section_title("核心功能模块")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        card("非遗教学", "通过图文、短视频和课程模块提升大众认知与学习参与度。")
    with c2:
        card("在线商城", "支持文创、礼盒、收藏品等不同产品的展示、导购与销售转化。")
    with c3:
        card("社区互动", "构建作品分享、用户交流、活动参与和内容传播的互动空间。")
    with c4:
        card("共创传播", "结合直播、联名、活动与AR玩法扩大品牌影响力和社群参与度。")

    st.divider()

    z1, z2, z3 = st.columns(3)
    with z1:
        st.image(img_path("ar-demo.png"), use_container_width=True)
        st.markdown("### AR互动体验")
        st.write("增强产品内容表达，让非遗传播更具沉浸感和互动感。")
    with z2:
        st.image(img_path("live-stream.png"), use_container_width=True)
        st.markdown("### 直播传播")
        st.write("拓宽展示和销售渠道，增强实时互动能力与转化效率。")
    with z3:
        st.image(img_path("brand-video.png"), use_container_width=True)
        st.markdown("### 品牌内容输出")
        st.write("通过短视频与视觉内容讲好铁画故事，构建持续传播的品牌形象。")

st.markdown(
    """
    <div class="footer-box">
        合肥工业大学 · 铁火新生项目团队<br>
        非遗活化 · 材料创新 · 数字赋能
    </div>
    """,
    unsafe_allow_html=True,
)