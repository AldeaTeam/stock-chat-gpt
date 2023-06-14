# The journey to a private stock chatbot , with multiple LLMs options,  local deployment option, and web search function🔥🚀

This project is heavily inspired by many latest projects in the open-source community with an emphasis on [Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot) for this initial implementation. 

## Local  setup  
Win and Mac systems are tested.

- Clone the repository:
```
git clone https://github.com/AldeaTeam/stock-chat-gpt.git
```

- Navigate to the project directory:
```
cd stock-chat-gpt
```

- Setup a virtual environment:
```
conda create -n stockchat python== 3.10
```

- Install the required dependencies in the virtual environment and tsinghua mirror is strongly recommended!
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- Launch the chat service locally:
```
streamlit run src/Home.py
```

## On cloud 
**AutoDL service** is tested and the image will be provided:

- First input in the new terminal:
```
source activate 
```

- Then follow the instructions as stated above.

- For SSH channel question, please refer to the document or [the guide video from Bilibili](https://www.bilibili.com/opus/777675928761270272).


### Core functions and future devplan 
- [ ] LLM chat
- - OpenAI ✅
- - Local LLMs like GPT4all, TigerBot... 
- [ ] Local knowledge base, vector storage and query  
- - Csv, pdf, txt file are supported ✅
- - Graph date to be supported
- [ ] External web search
- [ ] Data visualization and exploration
- [ ] One-click installation
- [ ] And more 😄. 
- [ ] Any comments or suggestions will be appreciated.


### A record of our efforts and experience.
- ref/stockchat-brainstorm-plan shows our brainstorming process.
- ref/linux-deploy-guide.pdf shows the mistakes and how-to-fix guide for linux deployment of [LangChain-ChatGLM project](https://github.com/imClumsyPanda/langchain-ChatGLM).
- A list of some key open-source projects from which we've gained helpful inspirations are listed below. Many thanks to those creative contributors. 👏🏻👏🏻

## 记“可私有化部署、切换不同LLM的股票聊天机器人”的学习、开发历程 20230614😂😄

项目最初目标是参考Finchat等应用的功能搭建具备本地PDF总结问答、web搜索总结等功能的股票分析助手，可选用多种LLM模型或商业API。

在社区提供的课程学习基础上，在社区小伙伴的❤️献言献策❤鼓励中以及特别指导 - [社恐杨老师](https://github.com/pzc163)的因材施教、渐进式指导下，（完全没有LLM或编程/产品开发经验的）本小组成员们先后观摩学习了不同的开源项目，从中汲取思路并反复尝试，最后放弃了开源社区比较成熟的LangChain-ChatGLM（虽然基本契合项目开发目标，但环境依赖包略多、配置容易冲突😂），转而专注**通过少数框架和工具包，完成核心功能的实现。**
- 项目计划和头脑风暴示意见 ref/stockchat-brainstorm-plan.
- [LangChain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM) 的linux部署和易错问题 见 ref/linux-deploy-guide.pdf
- [AutoDL新webUI访问（SSH隧道访问）](https://www.bilibili.com/opus/777675928761270272)
- 重要参考项目见下表，感谢他们为开源社区的用爱发电👏🏻👏🏻~ ~

### 核心功能和未来开发计划
- [ ] LLM 对话
- - 商业API 如 openAI ✅
- - 开源本地部署的LLM 如 GPT4all, TigerBot... 
- [ ] 本地知识库导入、向量化存储和查询 
- - 支持 CSV, PDF, TXT 格式文件✅
- - 支持图数据
- [ ] 外部搜索功能
- [ ] 数据可视化展示和分析模块
- [ ] 一键安装包
- [ ] 待补充，欢迎任何建议和意见~~


### 参考项目
- [Robby-Chat](https://github.com/yvann-hub/Robby-chatbot)
- [PrivateGPT](https://github.com/imartinez/privateGPT)
- [Serge - 一键安装丝滑](https://github.com/nsarrazin/serge)
- [DB-GPT - 支持多种模型、借鉴数据处理](https://github.com/csunny/DB-GPT)
- [LangChain-ChatGLM-&-TigerBot - 经典本地知识库问答项目](https://github.com/wordweb/langchain-ChatGLM-and-TigerBot)
- [TigerBot-以世界级的基础大模型，贡献于中国式的创新](https://github.com/TigerResearch/TigerBot)

### 致谢
- 本次初步实施的核心成员： [KuangJunWei -自学成才的“电工”](https://github.com/kuangjunwei1) -感谢经验并不丰富的邝大佬从代码解析到断点测试亲历亲为并及时辅导小白组长😂，感谢探索模型云端部署的[It-five同学-NLP专家](https://github.com/IT-five)，本组实力后续才能充分发挥的[BlankZhou- 后端-搜索部分](https://github.com/zhou-yi-git)，[DoubleShan-量化/数据分析](https://github.com/shanshan-he/)， [EricJiang-数据分析](https://github.com/EricJiang0423)；以及本组特邀的专家指导级组员安阳大佬等人；
- 特别感谢其他小组的热心同学比如[大肚烟斗](https://github.com/light-124)，[Ryan-芦苇大佬](https://github.com/chi7cha7rito)，[善行大神](https://github.com/wordweb)等人（肯定有疏漏❤❤）。。
- 再次感谢[热心不社恐的杨老师](https://github.com/pzc163) （被 [组长Sarai小白](https://github.com/SaraiQX) “螺旋式”下调预期😝）提供包括基础知识的耐心指导~
- 最后感谢[DataWhale社区](https://github.com/datawhalechina)的辛苦组织和推动，感谢Magic杨老师等助教老师调动了良好的学习和讨论氛围~~ 感谢赞助商~~


