# 很棒的基于位置的量子密码学 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
这是关于基于位置的量子密码学 (PBQC) 的精选论文列表。目标是为这个不断发展的领域建立一个分类的、社区驱动的、始终最新的文献概述。

QPV = 量子位置验证

QPA = 基于位置的量子身份验证

PB-QKD = 基于位置的量子密钥分配

## 内容

- [经典的不可能](#classical-impossibility)
- [第一个协议](#first-protocols)
- [QPV 的普遍攻击](#universal-attacks-on-qpv)
- [应对 QPV 普遍攻击的方法](#ways-around-the-universal-attacks-on-qpv)
- [猜想的指数下界](#conjectured-exponential-lower-bound)
- [基于量子位置的身份验证](#quantum-position-based-authentication)
- [理解 NLQC](#towards-understanding-nlqc)
- [走向实用](#towards-practicality)
- [Experiments](#experiments)

## 经典的不可能

- [Position-based cryptography (2009)](https://doi.org/10.1007/978-3-642-03356-8_23) - 在普通模型中建立了基于位置的密码学的经典不可能性。探索有界存储模型的可能性。

## 第一个协议

- [Tagging systems (2006)](https://patents.google.com/patent/US20060022832A1/en) - 以“量子标记”的名义推出 QPV。
- [使用位置相关的通信
量子纠缠 (2010)](https://doi.org/10.1103/PhysRevA.81.042319) - 在学术文献中介绍了 QPV，但错误地声称无条件安全。基于贝尔状态研究 QPV。
- [Quantum location verification in noisy channels (2010)](https://doi.org/10.1109/GLOCOM.2010.5684009) - 研究基于贝尔态、GHZ态和纠缠交换的QPV。研究噪声/退相干的影响。
- [Quantum tagging: Authenticating location via quantum information and relativistic signalling constraints (2011)](https://doi.org/10.1103/PhysRevA.84.012326) - 引入了一系列不同的 QPV 协议，例如 BB84 QPV、$f$-routing、$f$-BB84 QPV 及其变体。提到对其中一些的基于纠缠的攻击。

### BB84 QPV 和概括

- [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - 显示针对非缠结攻击的安全性。
- [A monogamy-of-entanglement game with applications to device-independent quantum cryptography (2013)](https://doi.org/10.1088/1367-2630/15/10/103002) - 显示非纠缠攻击、并行重复的严格上限和重复协议的线性下限。
- [Practical position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.92.052304) - 考虑两个输入基通过单一 $U$ 相关的情况。
- [A tight lower bound for the BB84-states quantum-position-verification protocol (2015)](https://arxiv.org/abs/1504.07171) - 为经典通信的攻击提供了本质上严格的下限。
- [Loss-tolerant position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.91.042337) - 将 BB84 QPV 推广到更多输入基础，并因此获得更好的损耗容限特性。还讨论了 BB84 QPV 中诱饵状态和连续变量的使用。
- [Position-based quantum cryptography and catalytic computation (2016)](https://eprints.illc.uva.nl/id/eprint/2138/) - 第 5 章独立地将 BB84 QPV 推广到更多输入基础。第 4 章提供了对基于交错酉协议的有效攻击。
- [Breaking simple quantum position verification protocols with little entanglement (2020)](https://arxiv.org/abs/2007.15808) - 考虑输入碱基通过不同角度相关的情况，并根据角度显示与维度相关的攻击。值得注意的是，它们表明角度 $\pi/6$ （在 Clifford 层次结构之外）可以受到 6 维资源状态的攻击。
- [Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers (2023)](https://doi.org/10.1103/PhysRevLett.131.140802) - 根据丢失率和错误率严格描述协议的安全区域。
- [Security of a continuous-variable based quantum position verification protocol (2023)](https://arxiv.org/abs/2308.04166) - 将协议推广到连续变量输入，并根据丢失率和噪声率显示针对非纠缠攻击的安全性。
- [Perfect cheating is impossible for single-qubit position verification (2024)](https://arxiv.org/abs/2406.20022) - 考虑一种概括，其中输入量子位是随机均匀选择的 $\mathbb{C}^2$ 投影仪的本征态。表明没有有限维资源状态可以完美地攻击该协议。

### $f$-路由

- [The garden-hose model (2013)](https://doi.org/10.1145/2422436.2422455) - 研究对 $f$ 路由的攻击，并引入花园软管复杂性，将对 $f$ 路由的攻击与复杂性理论联系起来。提供了有关该连接的许多初步结果，例如任何 $f \in \mathsf{L}$ （经过预处理）都可以被有效地攻击。
- [A single-qubit position verification protocol that is secure against multi-qubit attacks (2022)](https://doi.org/10.1038/s41567-022-01577-0) - 显示攻击资源状态维度的稳健线性下界。
- [Code-routing: A new attack on position verification (2023)](https://doi.org/10.22331/q-2023-08-09-1079) - 提供对 $f$ 路由的新攻击，将攻击连接到秘密共享方案和跨度程序，并表明任何 $f \in \mathsf{Mod}_p\mathsf{L}$ （经过预处理），对于 $p$ 素数，都可以被有效地攻击。
- [Relating non-local quantum computation to information theoretic cryptography (2023)](https://doi.org/10.22331/q-2024-06-27-1387) - 将 $f$ 路由与经典密码学中的主题连接起来，特别是有条件的秘密披露。显示任何 $f$ 的攻击的次指数上限，并找到一个被认为位于 $\mathsf{P}$ 之外（经过预处理）但有效攻击的 $f$。
- [Rank lower bounds on non-local quantum computation (2024)](https://arxiv.org/abs/2402.18647) - 为完美攻击提供资源状态施密特等级的下限。给出一些具体函数的线性下界。
- [Linear gate bounds against natural functions for position-verification (2024)](https://arxiv.org/abs/2402.18648) - 提供攻击内积函数所需的量子门/测量数量的稳健线性下界。

### $f$-BB84 QPV

- [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - 仔细考虑更高维度的 QPV，并在随机预言模型中显示出无条件的安全性。
- [A single-qubit position verification protocol that is secure against multi-qubit attacks (2022)](https://doi.org/10.1038/s41567-022-01577-0) - 显示攻击资源状态维度的稳健线性下界。
- [Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers (2023)](https://doi.org/10.1103/PhysRevLett.131.140802) - 根据丢失率和错误率严格描述协议的安全区域。
- [Making existing quantum position verification protocols secure against arbitrary transmission loss (2023)](https://arxiv.org/abs/2312.12614) - 在 QPV 中引入额外的承诺步骤，并表明对于涉及 $f$-BB84 QPV 的一类协议，这使得传输损耗与安全性无关。认为$f$-BB84是一个实用的QPV协议。
- [Continuous-variable quantum position verification secure against entangled attackers (2024)](https://arxiv.org/abs/2404.14261) - 将 $f$-BB84 QPV 推广到连续变量输入，并显示与有限维输入类似的安全声明。

### 贝尔QPV

- [使用位置相关的通信
量子纠缠 (2010)](https://doi.org/10.1103/PhysRevA.81.042319) - 基于贝尔态研究 QPV。声称无条件安全，后来证明是假的。
- [Quantum location verification in noisy channels (2010)](https://doi.org/10.1109/GLOCOM.2010.5684009) - 研究基于贝尔态、GHZ态和纠缠交换的QPV。研究噪声/退相干的影响。
- [基于立场的不安全感
针对纠缠攻击的量子加密协议 (2011)](https://doi.org/10.1103/PhysRevA.83.012322) - 证明了之前声称安全的 QPV 协议的不安全性，并研究了纠缠攻击的一般原理。研究基于 Bell/GHZ 状态的 QPV 协议的变体，并表明使用泡利 $X$、$Y$、$Z$ 以外的本征态会导致需要 >1 个 EPR 对才能受到攻击的协议。
- [Loss-tolerant quantum secure positioning with weak laser sources (2016)](https://doi.org/10.1103/PhysRevA.94.032315) - 研究具有可分离输入的协议版本。证明完全的丢失容忍度并研究基于诱饵状态的实际实施。
- [On the role of quantum communication and loss in attacks on quantum position verification (2022)](https://arxiv.org/abs/2208.04341) - 证明非纠缠攻击成功概率的上限为 3/4。
- [Monogamy of highly symmetric states (2023)](https://arxiv.org/abs/2309.16655) - 本文的结果意味着非纠缠攻击成功概率的上限为 $\ln(2) \approx 0.69$。

### 其他协议

- [Practical position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.92.052304) - 提供基于交错酉的协议，推测安全性。后来该协议被有效地破解。
- [Quantum position verification in bounded-attack-frequency model (2016)](https://doi.org/10.1007/s11433-016-0234-0) - 考虑输入信息非同时到达证明者的 BB84 QPV（根据哪一侧先到达进行编码）。在此设置中讨论基于端口的一般攻击。
- [Practically secure quantum position verification (2021)](https://doi.org/10.1088/1367-2630/ac0755) - 概述当时现有的协议，并混合其中的元素以获得这些协议的不同变体。
- [Towards practical and error-robust quantum position verification (2021)](https://arxiv.org/abs/2106.12911) - 定义了一种基于SWAP测试的新协议，并对其进行了理论和实践研究。
- [Making existing quantum position verification protocols secure against arbitrary transmission loss (2023)](https://arxiv.org/abs/2312.12614) - 在 QPV 中引入额外的承诺步骤，并表明对于一类协议，这使得传输损耗与安全性无关。

## QPV 的普遍攻击

- [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - 严格定义 QPV，并使用输入量子位数量中双指数数量的预共享 EPR 对来对所有此类 QPV 协议进行一般攻击。
- [Simplified instantaneous non-local quantum computation with applications to position-based cryptography (2011)](https://doi.org/10.1088/1367-2630/13/9/093036) - 使用输入量子比特数量呈指数级数量的预共享 EPR 对，对基于端口的隐形传态的 QPV 进行一般攻击。还提供了具有可证明线性下限的 QPV 协议。
- [Instantaneous non-local computation of low T-depth quantum circuits (2016)](https://doi.org/10.4230/LIPIcs.TQC.2016.9) - 基于将任务酉分解为 Clifford+T 门的电路，使用 T 门数量或 T 深度中指数数量的预共享 EPR 对对 QPV 进行一般攻击。
- [Non-local computation of quantum circuits with small light cones (2022)](https://arxiv.org/abs/2203.10106) - 基于任务酉电路分解的几何结构，提供了对 QPV 的一般攻击。对于某些类别的酉元攻击比以前的一般攻击更有效。

### 对酉类的攻击

- [Practical position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.92.052304) - 显示对某些类别的有效攻击，例如 Clifford 层次结构的第二级。
- [Bounds on instantaneous non-local quantum computation (2020)](https://doi.org/10.1109/TIT.2019.2950190) - 表明使用 $\log(1/\varepsilon)$ EPR 对可以攻击任何 2 量子位酉，直至错误 $\varepsilon$，并且可以使用 1 个 EPR 对攻击任何厄米二分二元控制酉。显示一般二分二元控制酉的纠缠熵的对数下界。

## 应对 QPV 普遍攻击的方法

- [Quantum tagging for tags containing secret classical data (2011)](https://doi.org/10.1103/PhysRevA.84.022335) - 当验证者和证明者预先共享秘密时，在设置中考虑 QPV。表明通过使用 QKD 无限扩展秘密，QPV 是无条件安全的。
- [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - 显示随机预言模型中 $f$-BB84 QPV 的无条件安全性。
- [Beating classical impossibility of position verification (2022)](https://doi.org/10.4230/LIPIcs.ITCS.2022.100) - 根据 LWE 是量子困难的假设，构造仅使用经典输入和输出信息的 QPV 协议。显示随机预言模型中的无条件安全性。

## 猜想的指数下界

- [Geometry of Banach spaces: A new route towards position based cryptography (2021)](https://doi.org/10.1007/s00220-022-04407-9) - 提供基于根据经典输入信息应用相位酉的新协议。显示了攻击规律性假设下的指数下界，以及以尚未解决的巴拿赫空间几何猜想为条件的指数下界。

## 基于量子位置的身份验证

- [Position-based quantum cryptography: Impossibility and constructions (2011)](https://doi.org/10.1137/130913687) - 提供从 QPV 到 QPA 再到 PB-QKD 的通用但低效的构造。
- [Quantum position verification in the random oracle model (2014)](https://doi.org/10.1007/978-3-662-44381-1_1) - 为 $f$-BB84 QPV 的随机预言模型中的 QPA 和 PB-QKD 提供更高效的扩展。
- [Quantum Secure Key Exchange with Position-based Credentials (2025)](https://arxiv.org/abs/2506.03549) - 改进了如何使用 QPV 在 QKD 内提供身份验证的分析。
 
## 理解 NLQC

- [Quantum tasks in Minkowski space (2012)](https://doi.org/10.1088/0264-9381/29/22/224013) - 考虑比 QPV 更一般的量子任务。
- [Popescu-Rohrlich correlations imply efficient instantaneous nonlocal quantum computation (2016)](https://doi.org/10.1103/PhysRevA.94.022318) - 表明如果攻击者共享 PR 框，则仅使用线性纠缠和线性数量的 PR 框即可攻击任何单一体。
- [Constraining the doability of relativistic quantum tasks (2019)](https://arxiv.org/abs/1909.05403) - 将基于端口的攻击推广到更一般的量子任务和时空电路。发现任务的粗略因果结构是确定任务是否可非局部执行的相关属性。
- [On the role of quantum communication and loss in attacks on quantum position verification (2022)](https://arxiv.org/abs/2311.00677) - 表明任何可以与量子通信无关但可以安全抵御经典通信攻击的 QPV 协议都可以转变为可以安全抵御量子通信攻击的协议。另请注意，如果信号损失足够高，则任何 QPV 协议都可以通过微不足道的隐形传输攻击进行有效攻击。
- [Complexity and entanglement in non-local computation and holography (2022)](https://doi.org/10.22331/q-2022-11-28-864) - 请注意，必要的攻击资源需求由任务单元的纠缠部分控制。表明，对于一侧是经典输入信息的任务，双对数（后来改进为对数）下界和指数上限（根据您选择的任务酉的纠缠部分的任何复杂性度量）适用于攻击。
- [Relating non-local quantum computation to information theoretic cryptography (2023)](https://doi.org/10.22331/q-2024-06-27-1387) - 通过 $f$ 路由将 NLQC 连接到经典密码学中的一些协议。
- [Time-constrained local quantum state discrimination (2023)](https://arxiv.org/abs/2311.00677) - 研究非纠缠量子攻击和经典攻击对状态辨别 QPV 协议的区别，并证明了几个结果，例如，存在一个可以通过量子通信完美辨别的可分离状态系综，但并非没有。
- [基于位置的量子密码学的安全性通过全息术限制哈密顿模拟 (2024)](https://doi.org/10.1007/JHEP08(2024)152) - 将 QPV 连接到哈密顿模拟。表明如果可以为 QPV 攻击显示超线性下界，那么一个哈密顿量模拟另一哈密顿量所需的资源就有新的基本下界。
- [A complexity theory for non-local quantum computation (2025)](https://arxiv.org/abs/2505.23893) - 查找各种不同 NLQC 任务之间的关系，包括显示 $f$-routing 和 $f$-BB84 是等效的，并且它们之间的开销不断减少。

### 与全息术的连接

- [全息中的量子任务 (2019)](https://doi.org/10.1007/JHEP10(2019)233) - 通过注意到批量 QPV 协议必须在边界中具有等效协议，将 QPV 连接到 AdS/CFT 猜想。事实证明，边界实现是对批量 QPV 协议的有效攻击，非本地实现。
- [全息散射需要连接的纠缠楔(2020)](https://doi.org/10.1007/JHEP08(2020)132) - 进一步加强QPV和全息术之间的联系，并估计相关边界区域之间的互信息。由于本文的结果，基于猜想的结果可以对所有 QPV 协议产生有效的攻击。
- [Holography as a resource for non-local quantum computation (2022)](https://arxiv.org/abs/2210.13500) - 讨论并填补上面一篇论文中的漏洞。基于模拟全息 CFT 构建攻击，并认为基于某些假设，任何多项式复杂酉都可以被有效攻击。


## 走向实用

- [Loss-tolerant position-based quantum cryptography (2015)](https://doi.org/10.1103/PhysRevA.91.042337) - 将 BB84 QPV 推广到更多输入基础，并因此获得更好的损耗容限特性。还讨论了 BB84 QPV 中诱饵状态和连续变量的使用。
- [Loss-tolerant quantum secure positioning with weak laser sources (2016)](https://doi.org/10.1103/PhysRevA.94.032315) - 研究带有可分离输入的贝尔 QPV。证明完全的丢失容忍度并研究基于诱饵状态的实际实施。
- [Towards practical and error-robust quantum position verification (2021)](https://arxiv.org/abs/2106.12911) - 定义了一种基于SWAP测试的新协议，并对其进行了理论和实践研究。认为该协议具有实用且强大的特性。
- [Single-qubit loss-tolerant quantum position verification protocol secure against entangled attackers (2023)](https://doi.org/10.1103/PhysRevLett.131.140802) - 根据丢失率和错误率严格描述 BB84 QPV 和 $f$-BB84 QPV 的安全区域。
- [Security of a continuous-variable based quantum position verification protocol (2023)](https://arxiv.org/abs/2308.04166) - 将 BB84 QPV 推广到连续变量输入，并根据丢失率和噪声率显示针对非纠缠攻击的安全性。
- [Making existing quantum position verification protocols secure against arbitrary transmission loss (2023)](https://arxiv.org/abs/2312.12614) - 在 QPV 中引入额外的承诺步骤，并表明对于涉及 $f$-BB84 QPV 的一类协议，这使得传输损耗与安全性无关。认为$f$-BB84是一个实用的QPV协议。
- [Towards practical quantum position verification (2023)](https://arxiv.org/abs/2309.10070) - 深入研究实际 QPV 实现的一些技术硬件细节。
- [Continuous-variable quantum position verification secure against entangled attackers (2024)](https://arxiv.org/abs/2404.14261) - 将 $f$-BB84 QPV 推广到连续变量输入，并显示与有限维输入类似的安全声明。

## 实验

- [Towards experimental demonstration of quantum position verification using single photons (2025)](https://doi.org/10.1088/2058-9565/adf2da) - 使用 SWAP 协议的 QPV 首次演示实验，其中来自光学微腔中单个半导体量子点的单光子。
