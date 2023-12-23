# 利用大语言模型对环境智能预测与可持续发展



**项目简介：**我们的项目旨在利用大型语言模型的强大分析和预测能力，为环境保护和可持续发展领域提供前沿的解决方案。通过整合环境数据、AI分析和教育推广，我们致力于：

1. **数据驱动的环境保护决策：** 运用先进的数据分析技术，为政府和企业提供准确、及时的环境数据和趋势分析，帮助其制定更有效的环保政策和可持续发展规划。

   

2. **公众环保意识的提升：** 建立交互式的教育平台，通过大型语言模型生成的内容，向社区和公众传播环保知识，并促进个人参与可持续行动的意识提升。

   

3. **环境变化的预测与应对：** 利用AI技术分析环境数据，预测自然灾害和气候变化趋势，为社区提供及时的预警和应对方案，减少可能的损失。

   

**项目愿景：** 我们希望通过技术创新和社会教育，促进环境保护和可持续发展理念的普及与实践，为建设更健康、更可持续的未来贡献我们的力量。



# 如何运行：



首次运行需要进行API设置，可以使用免费API，[水龙头API](https://faucet.openkey.cloud/)



API接口设置为： `https://openkey.cloud/v1/chat/completions`

获得的密钥填入KEY







# **项目展示：**

![img](https://raw.githubusercontent.com/wangshao2003/resourse/main/main.png)

![API设置.png](https://github.com/wangshao2003/resourse/blob/main/API%E8%AE%BE%E7%BD%AE.png?raw=true)

![](https://raw.githubusercontent.com/wangshao2003/resourse/main/%E6%99%8B%E7%BA%A7%E8%B5%9B.png)









# 一、**作品研究背景**

 

随着全球环境问题日益严重，气候变化、环境污染和自然灾害等已经成为我们社会面临的重要挑战。在这种情况下，利用先进技术来促进环境保护和可持续发展变得尤为重要。然而，环境保护领域面临着一系列挑战，其中包括：

 

数据不完整性和碎片化： 环境数据通常来自多个来源，且格式各异，这导致了数据的碎片化和不完整性，给数据分析和决策带来了困难。

 

缺乏精准的环境预测： 尽管有大量的环境数据可供分析，但对于未来环境变化的准确预测仍然具有挑战性，尤其是在自然灾害和气候变化方面。

 

公众参与和意识缺失： 尽管环保意识在提高，但公众参与环保行动的积极性仍有提升空间。教育推广和信息传播在提高公众环保意识方面也有一定不足。

 

在这个背景下，大型语言模型的出现为解决这些挑战提供了新的可能性。这种模型的强大分析能力和语言生成功能，为环保领域的数据整合、预测分析和教育推广提供了新的思路和工具。

 

本作品旨在利用大型语言模型的优势，探索并解决环境保护领域面临的问题，从而推动环保意识的提高和可持续发展的实践。

 

 

 

# 二、作品应用场景（描述拟解决的核心问题）

 

**数据整合与预测分析：** 我们将空气质量整合并通过大型语言模型应用于环境数据的预测分析。通过整合来自不同来源的环境数据，我们可以更准确地预测气候变化、自然灾害等事件，提前采取必要的应对措施。

 

**环保决策支持：** 我们的作品将为政府机构、环保组织以及企业提供数据驱动的环保决策支持。我们的系统将帮助制定更有效的环保政策和措施，以最大程度地保护环境。

 

**公众参与和教育推广：** 我们计划建立一个交互式的环保教育平台，利用大型语言模型生成个性化的环保信息和教育内容。通过互动体验和知识传播，我们希望提高公众对环保问题的认知，并激发个人参与环保行动的意愿。

 

**环境监测与警示：** 我们的系统将实时监测环境数据，提供警示和建议。这有助于社区和政府及时应对环境变化带来的风险。

 

通过在这些应用场景中运用大型语言模型的技术优势，我们旨在解决环境保护领域面临的数据碎片化、预测准确性和公众参与度等核心问题，推动环保和可持续发展取得实质性进展。

 

 

 

# **三、功能概述（阐述作品的主要功能、特色、核心优势）**

 

 **主要功能：**作品能够整合来自不同来源的环境数据，利用大型语言模型的强大分析能力对数据进行处理和分析，提供全面的环境状况评估和预测分析。

 

 **特色：**我们的作品利用大型语言模型技术，能够根据用户的兴趣和需求生成个性化的环保教育内容和建议，提供符合用户需求的定制化服务，增强用户参与度。我们的作品注重可持续性发展，设计具有可扩展性，能够灵活适应不同规模和需求的环境保护项目，并持续为环保事业做出贡献。

 

**核心优势：**

AI技术优势： 大型语言模型的应用为我们带来了更高效、更准确的数据处理和预测能力，为环保领域提供了新的解决方案。

综合性解决方案： 作品将数据获取，环境分析，环境保护建议等多个功能融合于一体，为环保领域提供全方位的解决方案。

 

 

 

 

 

 

 

# **四、设计开发（系统方案、核心技术及创新创意等）**

 

**系统方案：**

选择城市和省份： 通过下拉框选择特定的省份和城市，用于确定查询的地理位置。

调用和风天气 API： 根据用户选择的城市，调用和风天气 API 获取实时空气质量信息。

整合 ChatGPT API： 将获取的空气质量信息传递给 ChatGPT API 进行分析，并获取生成的建议。

展示空气质量和建议： 在界面上展示获取的空气质量信息和 ChatGPT 生成的建议。

 

**核心技术：**

Tkinter： 这是 Python 的标准 GUI 库，用于创建应用的用户界面。、

 

Ttkbootstrap：Tkinter主题扩展，用于美化程序的GUI界面

 

和风天气 API： 用于获取实时的空气质量信息，包括空气质量指数、主要污染物、PM2.5 和其他空气质量数据。

 

ChatGPT API： 这是一个人工智能大语言模型，可以生成文本并提供建议。你将用户选择的城市的空气质量信息传递给 ChatGPT，以获取分析后的建议。

 

API存储： API的密钥属于隐私信息，使用本地文件来存储 API 密钥，以便安全地使用和存储这些敏感信息。

 

创新创意：

 将传统的环境质量与人工智能大语言模型结合利用大型语言模型的强大分析能力对数据进行处理和分析，提供全面的环境状况评估和预测分析。

 

 

 

 

 

 

 

# 五、**应用前景**

 

**用户增长和社区参与**： 通过提供个性化的空气质量信息和建议，可以吸引更多的用户加入平台。建立一个社区，让用户分享信息、经验和行动，将有助于增加参与度。

 

**教育和意识提升：** 此应用可以成为一个环保意识提升的工具。通过提供实时的空气质量数据和相关建议，促进用户更多地了解环境问题，并激发他们采取积极的环保行动。

 

**可持续发展：** 通过持续改进和更新，确保应用在技术、数据和用户体验上保持领先地位。这样能够为应用的长期发展和可持续性打下坚实基础。促进环保和健康意识的平台。持续不断地改进和扩展功能，能够使其在市场中保持竞争力，并为用户和社区带来更多实际价值。

 

**接入社交平台**：可以将此应用接入微信公众号等平台，使更多人能接触到环境信息并根据给出的建议为环境改善采取环保行动

 

 

 

 

# **六、改进方案** 

 

**添加空气质量折线图展示**：通过和风天气API空气质量预报，对未来五天的空气质量数据收集，添加matplotlib.pyplot库创建折线图展示空气质量，更直观的表现出未来当地的质量情况，让用户可以更清晰地对比和分析。可以选择不同城市或地区的数据展示，让用户能够比较不同地点的空气质量趋势。
