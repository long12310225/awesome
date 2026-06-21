# 很棒的激光雷达 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

<img src="img/lidar02.svg" align="right" width="200" alt="LIDAR" />

> 出色的激光雷达传感器及其应用的精选列表。

[LIDAR](https://en.wikipedia.org/wiki/Lidar) 是一种遥感传感器，使用激光以 ~cm 精度测量周围环境。传感数据通常称为点云，即 3D 或 2D 数据点集。该列表包含硬件、数据集、点云处理算法、点云框架、模拟器等。

欢迎贡献！请[查看](contributing.md)我们的指南。

> [!提示]
> 可选视图：[szenergy.github.io/awesome-lidar](https://szenergy.github.io/awesome-lidar/)
>
> 源代码：[github.com/szenergy/awesome-lidar](https://github.com/szenergy/awesome-lidar)

## 内容

- [很棒的激光雷达 ](#awesome-lidar-)
  - [Contents](#contents)
  - [Conventions](#conventions)
  - [Manufacturers](#manufacturers)
  - [Datasets](#datasets)
  - [Libraries](#libraries)
  - [Frameworks](#frameworks)
  - [Algorithms](#algorithms)
    - [基本匹配算法](#basic-matching-algorithms)
    - [语义分割](#semantic-segmentation)
    - [地面分割](#ground-segmentation)
    - [同时定位和建图 SLAM 和基于 LIDAR 的里程计和/或建图 LOAM](#simultaneous-localization-and-mapping-slam-and-lidar-based-odometry-and-or-mapping-loam)
    - [物体检测和物体跟踪](#object-detection-and-object-tracking)
    - [LIDAR-其他传感器校准](#lidar-other-sensor-calibration)
  - [Simulators](#simulators)
  - [相关精彩](#related-awesome)
  - [Others](#others)

## 惯例

- 任何带有 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube) 徽章的列表项都包含 YouTube 视频或频道
- 任何带有 ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar) 徽章的列表项都有科学论文或详细描述
- 任何带有 ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros) 徽章的列表项均与 [`ROS 2`](https://docs.ros.org/) 兼容
- 任何带有 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github) 徽章的列表项都有 GitHub 存储库或组织，星数徽章 ![](https://img.shields.io/github/stars/szenergy/awesome-lidar?color=yellow&style=flat-square&logo=github) 显示了存储库的受欢迎程度


## 制造商

- [Velodyne](https://velodynelidar.com/) - Ouster 和 Velodyne 宣布成功完成平等“合并”，于 2023 年 2 月 10 日生效。Velodyne 是一家机械和固态激光雷达制造商。总部位于美国加利福尼亚州圣何塞。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/user/VelodyneLiDAR)
- [ROS 驱动程序！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ros-drivers/velodyne) ![](https://img.shields.io/github/stars/ros-drivers/velodyne?color=yellow&style=flat-square&logo=github)
- [C++/Python 库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/valgur/velodyne_decoder) ![](https://img.shields.io/github/stars/valgur/velodyne_decoder?color=yellow&style=flat-square&logo=github)
- [Ouster](https://ouster.com/) - 激光雷达制造商，专注于数字旋转激光雷达。 Ouster 总部位于美国旧金山。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/Ouster-lidar)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ouster-lidar) ![](https://img.shields.io/github/stars/ouster-lidar?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Livox](https://www.livoxtech.com/) - 激光雷达制造商。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCnLpB5QxlQUexi40vM12mNQ)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Livox-SDK) ![](https://img.shields.io/github/stars/Livox-SDK?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [SICK](https://www.sick.com/ag/en/) - 传感器和自动化制造商，总部位于德国瓦尔德基希。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/user/SICKSensors)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/SICKAG) ![](https://img.shields.io/github/stars/SICKAG?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Hokuyo](https://www.hokuyo-aut.jp/) - 传感器和自动化制造商，总部位于日本大阪。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCYzJXC82IEy-h-io2REin5g)
- [Pioneer](http://autonomousdriving.pioneer/en/3d-lidar/) - 激光雷达制造商，专注于基于 MEMS 镜面的光栅扫描激光雷达（3D-LiDAR）。先锋公司总部位于日本东京。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/user/PioneerCorporationPR)
- [Luminar](https://www.luminartech.com/) - 专注于紧凑型汽车级传感器的激光雷达制造商。 Luminar 总部位于美国加利福尼亚州帕洛阿尔托。
- [Vimeo 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://vimeo.com/luminartech)
- [GitHub 组织！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/luminartech) ![](https://img.shields.io/github/stars/luminartech?color=yellow&style=flat-square&logo=github)
- [Hesai](https://www.hesaitech.com/) - 禾赛科技是一家激光雷达制造商，成立于中国上海。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCG2_ffm6sdMsK-FX8yOLNYQ/videos)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/HesaiTechnology) ![](https://img.shields.io/github/stars/HesaiTechnology?color=yellow&style=flat-square&logo=github)
- [Robosense](http://www.robosense.ai/) - RoboSense（速腾创新科技有限公司）是一家位于中国深圳和北京的激光雷达传感器、人工智能算法和 IC 芯片组制造商。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCYCK8j678N6d_ayWE_8F3rQ)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/RoboSense-LiDAR) ![](https://img.shields.io/github/stars/RoboSense-LiDAR?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [LSLIDAR](https://www.lslidar.com/) - LSLiDAR（雷神智能系统有限公司）是一家位于中国深圳的激光雷达传感器制造商和完整解决方案提供商。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/@lslidar2015)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Lslidar) ![](https://img.shields.io/github/stars/Lslidar?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Ibeo](https://www.ibeo-as.com/) - Ibeo Automotive Systems GmbH 是一家汽车工业/环境检测激光扫描仪/LIDAR 制造商，总部位于德国汉堡。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/IbeoAutomotive/)
- [Innoviz](https://innoviz.tech/) - Innoviz Technologies / 专注于固态激光雷达。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCVc1KFsu2eb20M8pKFwGiFQ)
- [Quanenergy](https://quanergy.com/) - Quanenergy Systems / 固态和机械 LIDAR 传感器 / 提供测绘、工业自动化、运输和安全领域的端到端解决方案。总部位于美国加利福尼亚州桑尼维尔市。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/QuanergySystems)
- [Cepton](https://www.cepton.com/index.html) - Cepton（Cepton Technologies, Inc.）/无摩擦、无反光镜设计先驱，自主研发MMT（微动技术）激光雷达技术。总部位于美国加利福尼亚州圣何塞。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCUgkBZZ1UWWkkXJ5zD6o8QQ)
- [Blickfeld](https://www.blickfeld.com/) - Blickfeld 是一家面向自动驾驶移动和物联网的固态激光雷达制造商，总部位于德国慕尼黑。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/BlickfeldLiDAR)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Blickfeld) ![](https://img.shields.io/github/stars/Blickfeld?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Neuvition](https://www.neuvition.com/) - Neuvition 是一家位于中国吴江的固态激光雷达制造商。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UClFjlekWJo4T5bfzxX0ZW3A)
- [Aeva](https://www.aeva.com/) - Aeva 正在将下一波感知技术引入自动驾驶、消费电子、健康、工业机器人和安全领域的所有设备，美国加利福尼亚州山景城。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/AevaInc)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/aevainc) ![](https://img.shields.io/github/stars/aevainc?color=yellow&style=flat-square&logo=github)
- [XenomatiX](https://www.xenomatix.com/) - XenomatiX 提供基于多光束激光器概念的真正固态激光雷达传感器。 XenomatiX 总部位于比利时鲁汶。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/@XenomatiXTruesolidstatelidar)
- [MicroVision](https://microvision.com/) - 作为基于 MEMS 的激光束扫描技术的先驱，主要致力于构建汽车级激光雷达传感器，位于德国汉堡。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/user/mvisvideo)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/MicroVision-Inc) ![](https://img.shields.io/github/stars/MicroVision-Inc?color=yellow&style=flat-square&logo=github)
- [PreAct](https://www.preact-tech.com/) - PreAct 的使命是让汽车行业及其他行业的生活更安全、更高效。总部位于美国俄勒冈州波特兰。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/@PreActTechnologies)
- [Pepperl+Fuchs](https://www.pepperl-fuchs.com/) - 是一家全球科技公司，专门从事创新自动化解决方案和传感器技术，例如激光雷达，总部位于德国曼海姆。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/pepperl-fuchs)
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/user/PepperlFuchsUSA)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PepperlFuchs) ![](https://img.shields.io/github/stars/PepperlFuchs?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Riegl](https://www.riegl.com/) - Riegl 是一家 3D 激光扫描系统制造商，总部位于奥地利。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/@RIEGLLIDAR)
- [GitHub 组织 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/riegllms) ![](https://img.shields.io/github/stars/riegllms?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
## 数据集

- [Ford Dataset](https://avdata.ford.com/) - 该数据集带有时间戳，包含来自所有传感器的原始数据、校准值、姿态轨迹、地面真实姿态和 3D 地图。数据与机器人操作系统 (ROS) 兼容。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2003.07969.pdf)
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Ford/AVData)![](https://img.shields.io/github/stars/Ford/AVData?color=yellow&style=flat-square&logo=github)
- [Audi A2D2 Dataset](https://www.a2d2.audi) - 该数据集具有 2D 语义分割、3D 点云、3D 边界框和车辆总线数据。
- [论文！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://www.a2d2.audi/content/dam/a2d2/dataset/a2d2-audi-autonomous-driven-dataset.pdf)
- [Waymo Open Dataset](https://waymo.com/open/) - 该数据集包含独立生成的激光雷达和相机数据标签，而不仅仅是投影。
- [Oxford RobotCar](https://robotcar-dataset.robots.ox.ac.uk/) - Oxford RobotCar 数据集包含 100 多次重复的穿过英国牛津的一致路线，这些路线是在一年多的时间内捕获的。
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/ORIOxfordRoboticsInstitute)
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://robotcar-dataset.robots.ox.ac.uk/images/RCD_RTK.pdf)
- [EU Long-term Dataset](https://epan-utbm.github.io/utbm_robocar_dataset/) - 该数据集是用我们的机器人汽车（当然是在人类驾驶模式下）收集的，配备了多达 11 个异构传感器，位于法国蒙贝利亚尔的市中心（用于长期数据）和郊区（用于环岛数据）。根据法国交通规则，车速限制在 50 公里/小时。
- [NuScenes](https://www.nuscenes.org/) - 自动驾驶的公共大规模数据集。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1903.11027.pdf)
- [Lyft](https://level5.lyft.com/dataset/) - 配备激光雷达和摄像头的福特 Fusion 车队收集的公共数据集。
- [KITTI](http://www.cvlibs.net/datasets/kitti/raw_data.php) - 广泛的公共数据集，主要关注计算机视觉应用，但也包含激光雷达点云。 ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Semantic KITTI](http://semantic-kitti.org/) - 用于语义和全景场景分割的数据集。
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=3qNOXvkpK4I)
- [CADC - Canadian Adverse Driving Conditions Dataset](http://cadcd.uwaterloo.ca/) - 恶劣天气条件（下雪天气）自动驾驶的公共大规模数据集。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2001.10117.pdf)
- [UofTPed50 Dataset](https://www.autodrive.utoronto.ca/uoftped50) - 多伦多大学，aUToronto 的自动驾驶汽车数据集，其中包含 GPS/IMU、3D LIDAR 和单目摄像头数据。它可用于 3D 行人检测。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1905.08758.pdf)
- [PandaSet Open Dataset](https://scale.com/open-datasets/pandaset) - Hesai & Scale提供的自动驾驶公共大规模数据集。它使研究人员能够使用真正的自动驾驶汽车的完整传感器套件来研究具有挑战性的城市驾驶情况。
- [Cirrus 数据集](https://developer.volvocars.com/open-datasets/cirrus/) 来自 LIDAR 扫描模式非均匀分布的公共数据集，重点是长距离。在此数据集中使用 Luminar Hydra LIDAR。该数据集可在沃尔沃汽车创新门户上获取。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2012.02938.pdf)
- [USyd Dataset- The Univerisity of Sydney Campus- Dataset](http://its.acfr.usyd.edu.au/datasets/usyd-campus-dataset/) - 1.5 年期间每周在悉尼大学校园及周边地区收集的长期、大规模数据集。它包括多种传感器模式并涵盖各种环境条件。 ROS兼容
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://ieeexplore.ieee.org/document/9109704)
- [布尔诺城市数据集！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Robotics-BUT/Brno-Urban-Dataset)![](https://img.shields.io/github/stars/Robotics-BUT/Brno-Urban-Dataset?color=yellow&style=flat-square&logo=github) - 捷克布尔诺自动驾驶汽车和自动机器人的导航和定位数据集。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://ieeexplore.ieee.org/document/9197277)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=wDFePIViwqY)
- [Argoverse ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://www.argoverse.org/) ![](https://img.shields.io/github/stars/argoai/argoverse-api?color=yellow&style=flat-square&logo=github) - 一个数据集，旨在支持自动驾驶车辆感知任务，包括 3D 跟踪和运动预测，收集于美国宾夕法尼亚州匹兹堡和佛罗里达州迈阿密。
- [论文！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://openaccess.thecvf.com/content_CVPR_2019/papers/Chang_Argoverse_3D_Tracking_and_Forecasting_With_Rich_Maps_CVPR_2019_paper.pdf)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=DM8jWfi69zM)
- [Boreas Dataset](https://www.boreas.utias.utoronto.ca/) - Boreas 数据集是通过在一年内重复行驶路线收集的，导致明显的季节性变化。 Boreas 总共包含超过 350 公里的驾驶数据，其中包括雨和大雪等恶劣天气条件下的多个序列。 Boreas 数据采集平台采用独特的高质量传感器套件，配有 128 通道 Velodyne Alpha Prime 激光雷达、360 度 Navtech 雷达，以及从 Applanix POSLV GPS/IMU 获得的准确地面真实姿态。
  - [纸📰](https://arxiv.org/abs/2203.10168)
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/utiasASRL/pyboreas)![](https://img.shields.io/github/stars/utiasASRL/pyboreas?color=yellow&style=flat-square&logo=github)

## 图书馆

- [Point Cloud Library (PCL)](http://www.pointclouds.org/) - 流行的高度并行编程库，具有大量工业和研究用例。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PointCloudLibrary/pcl)![](https://img.shields.io/github/stars/PointCloudLibrary/pcl?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Open3D library](http://www.open3d.org/docs/release/) - Open3D 库包含 3D 数据处理和可视化算法。它是开源的，支持 C++ 和 Python。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/intel-isl/Open3D) ![](https://img.shields.io/github/stars/intel-isl/Open3D?color=yellow&style=flat-square&logo=github)
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCRJBlASPfPBtPXJSPffJV-w)
- [PyTorch Geometric ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1903.02428.pdf) - PyTorch 的几何深度学习扩展库。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/rusty1s/pytorch_geometric)![](https://img.shields.io/github/stars/rusty1s/pytorch_geometric?color=yellow&style=flat-square&logo=github)
- [PyTorch3d](https://pytorch3d.org/) - PyTorch3d 是一个使用 3D 数据进行深度学习的库，由 Facebook AI Research 计算机视觉团队编写和维护。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/facebookresearch/pytorch3d)![](https://img.shields.io/github/stars/facebookresearch/pytorch3d?color=yellow&style=flat-square&logo=github)
- [Kaolin](https://kaolin.readthedocs.io/en/latest/) - Kaolin 是 NVIDIA Technologies 为游戏和应用程序开发人员编写的用于加速 3D 深度学习研究的 PyTorch 库。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/NVIDIAGameWorks/kaolin/) ![](https://img.shields.io/github/stars/NVIDIAGameWorks/kaolin?color=yellow&style=flat-square&logo=github)
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1911.05063.pdf)
- [PyVista](https://docs.pyvista.org/) - 通过可视化工具包的简化界面进行 3D 绘图和网格分析。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/pyvista/pyvista)![](https://img.shields.io/github/stars/pyvista/pyvista?color=yellow&style=flat-square&logo=github)
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://joss.theoj.org/papers/10.21105/joss.01450)
- [pyntcloud](https://pyntcloud.readthedocs.io/en/latest/) - Pyntcloud 是一个 Python 3 库，用于利用 Python 科学堆栈的强大功能处理 3D 点云。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/daavoo/pyntcloud)![](https://img.shields.io/github/stars/daavoo/pyntcloud?color=yellow&style=flat-square&logo=github)
- [pointcloudset](https://virtual-vehicle.github.io/pointcloudset/) - Python 库，用于有效分析随时间记录的大型点云数据集。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/virtual-vehicle/pointcloudset)![](https://img.shields.io/github/stars/virtual-vehicle/pointcloudset?color=yellow&style=flat-square&logo=github)
- [LAStools](https://rapidlasso.de/lastools/) - 用于点云处理和数据压缩的 C++ 库和命令行工具。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/LAStools/LAStools)![](https://img.shields.io/github/stars/LAStools/LAStools?color=yellow&style=flat-square&logo=github)

## 框架

- [Autoware](https://www.autoware.ai/) - 自动驾驶汽车学术和研究应用中的流行框架。
- [GitHub 组织结构 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/autowarefoundation) ![](https://img.shields.io/github/stars/autowarefoundation?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [纸![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://www.researchgate.net/profile/Takuya_Azumi/publication/327198306_Autoware _on_Board_Enabling_Autonomous_Vehicles_with_Embedded_Systems/links/5c9085da45851564fae6dcd0/Autoware-on-Board-Enabling-Autonomous-Vehicles-with-Embedded-Systems.pdf)
- [Baidu Apollo](https://apollo.auto/) - Apollo 是一个流行的框架，可加速自动驾驶汽车的开发、测试和部署。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ApolloAuto/apollo)![](https://img.shields.io/github/stars/ApolloAuto/apollo?color=yellow&style=flat-square&logo=github)
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/ApolloAuto)
- [ALFA Framework ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://ieeexplore.ieee.org/document/11024231) - 用于开发处理算法的开源框架，重点关注嵌入式平台和硬件加速。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github) ![](https://img.shields.io/github/stars/alfa-project/alfa-framework?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)](https://github.com/alfa-project/alfa-framework)

## 算法

### 基本匹配算法
- [迭代最近点 (ICP) ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=uzOCS_gdZuM) - 特征匹配应用程序 (ICP) 的必备算法。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/pglira/simpleICP) ![](https://img.shields.io/github/stars/pglira/simpleICP?color=yellow&style=flat-square&logo=github) - simpleICP C++ /Julia / Matlab / Octave / Python 实现。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ethz-asl/libpointmatcher) ![](https://img.shields.io/github/stars/ethz-asl/libpointmatcher?color=yellow&style=flat-square&logo=github) - libpointmatcher，实现 ICP 算法的模块化库。
- [Paper ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://link.springer.com/content/pdf/10.1007/s10514-013-9327-2.pdf) - libpointmatcher：比较真实数据集上的 ICP 变体。
- [正态分布变换！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=0YV4a2asb8Y) - 最新的大规模并行特征匹配方法 (NDT)。
- [KISS-ICP ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=kMMH8rA1ggI) - 捍卫点对点 ICP – 如果方法正确，注册简单、准确且稳健。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PRBonn/kiss-icp) ![](https://img.shields.io/github/stars/PRBonn/kiss-icp?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2209.15397.pdf)

### 语义分割
- [RangeNet++ ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/milioto2019iros.pdf) - 使用全卷积网络进行快速准确的 LiDAR 语义分割。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PRBonn/rangenet_lib)![](https://img.shields.io/github/stars/PRBonn/rangenet_lib?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=uo3ZuLuFAzk)
- [PolarNet ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2003.14032.pdf) - 在线 LiDAR 点云语义分割的改进网格表示。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/edward Zhou130/PolarSeg) ![](https://img.shields.io/github/stars/edwardzhou130/PolarSeg?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=iIhttRSMqjE)
- [Frustum PointNets ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1711.08488.pdf) - 用于从 RGB-D 数据检测 3D 对象的 Frustum PointNets。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/charlesq34/frustum-pointnets)![](https://img.shields.io/github/stars/charlesq34/frustum-pointnets?color=yellow&style=flat-square&logo=github)
- [Study of LIDAR Semantic Segmentation](https://larissa.triess.eu/scan-semseg/) - 基于扫描的 LiDAR 点云语义分割：实验研究 IV 2020。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/abs/2004.11803)
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](http://ltriess.github.io/scan-semseg)![](https://img.shields.io/github/stars/ltriess/scan-semseg?color=yellow&style=flat-square&logo=github)
- [LIDAR-MOS ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://www.ipb.uni-bonn.de/pdfs/chen2021ral-iros.pdf) - 3D LIDAR 数据中的移动对象分割
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PRBonn/LiDAR-MOS)![](https://img.shields.io/github/stars/PRBonn/LiDAR-MOS?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=NHvsYhk4dhw)
- [SuperPoint Graph ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1711.09869.pdf)- 使用超点图进行大规模点云语义分割
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/loicland/superpoint_graph)![](https://img.shields.io/github/stars/loicland/superpoint_graph?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=Ijr3kGSU_tU)
- [SuperPoint Transformer ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2306.08045.pdf)- 使用 Superpoint Transformer 进行高效 3D 语义分割
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/drprojects/superpoint_transformer)![](https://img.shields.io/github/stars/drprojects/superpoint_transformer?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=2qKhpQs9gJw)
- [RandLA-Net ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1911.11236.pdf) - 大规模点云的高效语义分割
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/QingyongHu/RandLA-Net) ![](https://img.shields.io/github/stars/QingyongHu/RandLA-Net?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=Ar3eY_lwzMk)
- [自动标记！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2108.13757.pdf) - 使用数据融合自动标记城市点云
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Amsterdam-AI-Team/Urban_PointCloud_Processing) ![](https://img.shields.io/github/stars/Amsterdam-AI-Team/Urban_PointCloud_Processing?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=qMj_WM6D0vI)

### 地面分割
- [Plane Seg ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ori-drs/plane_seg) ![](https://img.shields.io/github/stars/ori-drs/plane_seg?color=yellow&style=flat-square&logo=github) - ROS兼容的地平面分割；用于将平面拟合到激光雷达的库。
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=YYs4lJ9t-Xo)
- [LineFit Graph ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://ieeexplore.ieee.org/abstract/document/5548059)-水平 3D LiDAR 数据基于线拟合的快速地面分割
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/lorenwel/linefit_ground_segmentation)![](https://img.shields.io/github/stars/lorenwel/linefit_ground_segmentation?color=yellow&style=flat-square&logo=github)
- [Patchwork ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2108.05560.pdf)-基于区域平面拟合的 3D LiDAR 数据的稳健且快速的地面分割
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/LimHyungTae/patchwork) ![](https://img.shields.io/github/stars/LimHyungTae/patchwork?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=rclqeDi4gow)
- [Patchwork++ ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2207.11919.pdf)- Patchwork 的改进版本。 Patchwork++ 还为深度学习用户提供 pybinding
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/url-kaist/patchwork-plusplus-ros)![](https://img.shields.io/github/stars/url-kaist/patchwork-plusplus-ros?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=fogCM159GRk)
- [GSeg3D ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/html/2603.04208v1) - 针对安全关键型机器人和自动驾驶而设计的基于网格的 LiDAR 点云高精度地面分割。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/dfki-ric/ground_segmentation)![](https://img.shields.io/github/stars/dfki-ric/ground_segmentation?color=yellow&style=flat-square&logo=github)
- [ROS2集成！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/dfki-ric/ground_segmentation_ros2)![](https://img.shields.io/github/stars/dfki-ric/ground_segmentation_ros2?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=GXLTOoJbOhQ)

### 同时定位和建图 SLAM 和基于 LIDAR 的里程计和/或建图 LOAM
- [LOAM J. Zhang 和 S. Singh ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://youtu.be/8ezyhTAEyHs) - LOAM：实时激光雷达里程计和测绘。
- [LeGO-LOAM ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/RobustFieldAutonomyLab/LeGO-LOAM) ![](https://img.shields.io/github/stars/RobustFieldAutonomyLab/LeGO-LOAM?color=yellow&style=flat-square&logo=github) - 一款轻量级且适用于 ROS 兼容 UGV 的地面优化激光雷达测距和测绘 (LeGO-LOAM) 系统。
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=7uCxLUs9fwQ)
- 不同存储库上的 ROS 2 版本：[GitHub 存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/eperdices/LeGO-LOAM-SR) ![](https://img.shields.io/github/stars/eperdices/LeGO-LOAM-SR?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Cartographer ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/cartographer-project/cartographer) ![](https://img.shields.io/github/stars/cartographer-project/cartographer?color=yellow&style=flat-square&logo=github) - Cartographer 是 ROS 兼容系统，提供跨多个平台和传感器配置的 2D 和 3D 实时同步定位和建图 (SLAM)。 ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=29Knm-phAyI)
- [SuMa++ ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](http://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/chen2019iros.pdf) - 基于 LiDAR 的语义 SLAM。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PRBonn/semantic_suma/) ![](https://img.shields.io/github/stars/PRBonn/semantic_suma?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://youtu.be/uo3ZuLuFAzk)
- [OverlapNet ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](http://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/chen2020rss.pdf) - 基于 LiDAR 的 SLAM 的循环闭合。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PRBonn/OverlapNet)![](https://img.shields.io/github/stars/PRBonn/OverlapNet?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=YTfliBco6aw)
- [LIO-SAM ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2007.00258.pdf) - 通过平滑和映射实现紧耦合激光雷达惯性里程计。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/TixiaoShan/LIO-SAM) ![](https://img.shields.io/github/stars/TixiaoShan/LIO-SAM?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=A0H8CoORZJU)
- [删除！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](http://ras.papercept.net/images/temp/IROS/files/0855.pdf) - 删除，然后恢复：使用多分辨率范围图像构建静态点云地图。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/irapkaist/removt) ![](https://img.shields.io/github/stars/irapkaist/removt?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=M9PEGi5fAq8)
- [RESPLE ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2504.11580) - 基于 LiDAR 的里程计的递归样条估计
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ASIG-X/RESPLE) ![](https://img.shields.io/github/stars/ASIG-X/RESPLE?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=3-xLRRT25ys)
- [KISS-SLAM ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/kiss2025iros.pdf) - KISS-SLAM 是一个简单、强大且准确的 3D LiDAR SLAM 系统，可以正常工作。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PRBonn/kiss-slam)![](https://img.shields.io/github/stars/PRBonn/kiss-slam?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [FAST-LIO2 ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2010.08196) - 快速 LiDAR 惯性里程计是一种计算高效且强大的 LiDAR 惯性里程计软件包
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/hku-mars/FAST_LIO/tree/ROS2)![](https://img.shields.io/github/stars/hku-mars/FAST_LIO?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=2XNd7P6Qc2s)
- [MOLA ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://ingmec.ual.es/~jlblanco/papers/EMCEI_2024_Aguilar.pdf) - 用于定位和建图的模块化系统，提供 LiDAR 里程计 (LO)、LiDAR 惯性里程计 (LIO)、SLAM、仅本地化模式和地理参考。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/MOLAorg/mola) ![](https://img.shields.io/github/stars/MOLAorg/mola?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=sbakEOnsL6Y)

### 物体检测和物体跟踪
- [学习最佳分割点云！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/abs/1912.04976) - 作者：卡内基梅隆大学的 Peiyun Hu、David Held 和 Deva Ramanan。 IEEE 机器人与自动化快报，2020 年。
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=wLxIAwIL870)
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/peiyunh/opcseg)![](https://img.shields.io/github/stars/peiyunh/opcseg?color=yellow&style=flat-square&logo=github)
- [利用异方差任意不确定性实现稳健的实时 LiDAR 3D 物体检测！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1809.05590.pdf) - 作者：Di Feng、Lars Rosenbaum、Fabian Timm、Klaus迪特梅尔。第 30 届 IEEE 智能汽车研讨会，2019 年。
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=2DzH9COLpkU)
- [所见即所得：利用可见性进行 3D 对象检测！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1912.04986.pdf) - 作者：Peiyun Hu、Jason Ziglar、David Held、Deva Ramanan，2019 年。
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=497OF-otY2k)
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/peiyunh/WYSIWYG) ![](https://img.shields.io/github/stars/peiyunh/WYSIWYG?color=yellow&style=flat-square&logo=github)
- [urban_road_filter ![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://doi.org/10.3390/s22010194)-
适用于自动驾驶车辆的基于激光雷达的实时城市道路和人行道检测
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/jkk-research/urban_road_filter)![](https://img.shields.io/github/stars/jkk-research/urban_road_filter?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=T2qi4pldR-E)
- [由跟踪器检测![](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://www.semanticscholar.org/paper/3D-LIDAR-Multi-Object-Tracking-for-Autonomous-and-Rachman/bafc8fcdee9b22708491ea1293524ece9e314851) -用于自动驾驶的3D-LIDAR多目标跟踪：城市道路不确定性下的多目标检测和跟踪，也用于Autoware Universe
- [GitHub ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://autowarefoundation.github.io/autoware.universe/main/perception/detection_by_tracker/)![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=xSGCpb24dhI)

### LIDAR-其他传感器校准

- [direct_visual_lidar_calibration](https://koide3.github.io/direct_visual_lidar_calibration/) - 通用、单次、无目标、自动激光雷达相机外部校准工具箱
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/koide3/direct_visual_lidar_calibration)![](https://img.shields.io/github/stars/koide3/direct_visual_lidar_calibration?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://staff.aist.go.jp/k.koide/assets/pdf/icra2023.pdf)
- [OpenCalib ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/PJLab-ADG/SensorsCalibration) ![](https://img.shields.io/github/stars/PJLab-ADG/SensorsCalibration?color=yellow&style=flat-square&logo=github) - 多传感器校准工具箱自动驾驶
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/2205.14087)

## 模拟器
- [CoppeliaSim](https://www.coppeliarobotics.com/coppeliaSim) - 跨平台通用机器人模拟器（以前称为V-REP）。
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/user/VirtualRobotPlatform)
- [OSRF Gazebo](http://gazebosim.org/) - 基于OGRE的通用机器人模拟器，兼容ROS/ROS 2。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/osrf/gazebo) ![](https://img.shields.io/github/stars/osrf/gazebo?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [CARLA](https://carla.org/) - 基于虚幻引擎的汽车应用模拟器。兼容Autoware、百度Apollo和ROS/ROS 2。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/carla-simulator/carla)![](https://img.shields.io/github/stars/carla-simulator/carla?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UC1llP9ekCwt8nEJzMJBQekg)
- [LGSVL / SVL](https://www.lgsvlsimulator.com/) - 基于 Unity 引擎的汽车应用模拟器。兼容 Autoware、百度 Apollo 和 ROS/ROS 2。 *注：* LG 做出了艰难的决定，[暂停](https://www.svlsimulator.com/news/2022-01-20-svl-simulator-sunset) SVL Simulator 的积极开发。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/lgsvl/simulator)![](https://img.shields.io/github/stars/lgsvl/simulator?color=yellow&style=flat-square&logo=github)
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/c/LGSVLSimulator)
- [OSSDC SIM](https://github.com/OSSDC/OSSDC-SIM) - 基于Unity Engine的汽车应用模拟器，基于悬浮的LGSVL模拟器，但正在积极开发。兼容Autoware、百度Apollo和ROS/ROS 2。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/OSSDC/OSSDC-SIM)![](https://img.shields.io/github/stars/OSSSDC/OSSSDC-SIM?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=fU_C38WEwGw)
- [AirSim](https://microsoft.github.io/AirSim) - 基于虚幻引擎的无人机和汽车模拟器。与ROS兼容。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/microsoft/AirSim)![](https://img.shields.io/github/stars/microsoft/AirSim?color=yellow&style=flat-square&logo=github)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=gnz1X3UNM5Y)
- [AWSIM](https://tier4.github.io/AWSIM) - 基于 Unity 引擎的汽车应用模拟器。与 Autoware 和 ROS 2 兼容。
- [GitHub 存储库 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/tier4/AWSIM) ![](https://img.shields.io/github/stars/tier4/AWSIM?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=FH7aBWDmSNA)

## 相关精彩
- [很棒的点云分析！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Yo Chengliu/awesome-point-cloud-analysis#readme) ![](https://img.shields.io/github/stars/Yo Chengliu/awesome-point-cloud-analysis?color=yellow&style=flat-square&logo=github)
- [很棒的机器人！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Kiloreux/awesome-robotics#readme)![](https://img.shields.io/github/stars/Kiloreux/awesome-robotics?color=yellow&style=flat-square&logo=github)
- [很棒的机器人库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/jslee02/awesome-robotics-libraries#readme) ![](https://img.shields.io/github/stars/jslee02/awesome-robotics-libraries?color=yellow&style=flat-square&logo=github)
- [很棒的 ROS 2 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/fkromer/awesome-ros2#readme) ![](https://img.shields.io/github/stars/fkromer/awesome-ros2?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [真棒人工智能！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/owainlewis/awesome-artificial-intelligence#readme) ![](https://img.shields.io/github/stars/owainlewis/awesome-artificial-intelligence?color=yellow&style=flat-square&logo=github)
- [很棒的计算机视觉！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/jbhuang0604/awesome-computer-vision#readme) ![](https://img.shields.io/github/stars/jbhuang0604/awesome-computer-vision?color=yellow&style=flat-square&logo=github)
- [很棒的机器学习！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/josephmisiti/awesome-machine-learning#readme)![](https://img.shields.io/github/stars/josephmisiti/awesome-machine-learning?color=yellow&style=flat-square&logo=github)
- [很棒的深度学习！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/ChristosChristofidis/awesome-deep-learning#readme) ![](https://img.shields.io/github/stars/ChristosChristofidis/awesome-deep-learning?color=yellow&style=flat-square&logo=github)
- [很棒的强化学习！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/aikorea/awesome-rl/#readme)![](https://img.shields.io/github/stars/aikorea/awesome-rl?color=yellow&style=flat-square&logo=github)
- [很棒的 SLAM 数据集！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/youngguncho/awesome-slam-datasets#readme) ![](https://img.shields.io/github/stars/youngguncho/awesome-slam-datasets?color=yellow&style=flat-square&logo=github)
- [很棒的电子产品！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/kitspace/awesome- electronics#readme) ![](https://img.shields.io/github/stars/kitspace/awesome- electronics?color=yellow&style=flat-square&logo=github)
- [很棒的车辆安全和汽车黑客！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/jaredthecoder/awesome-vehicle-security#readme) ![](https://img.shields.io/github/stars/jaredthecoder/awesome-vehicle-security?color=yellow&style=flat-square&logo=github)
- [很棒的激光雷达相机校准！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Deephome/Awesome-LiDAR-Camera-Calibration) ![](https://img.shields.io/github/stars/Deephome/Awesome-LiDAR-Camera-Calibration?color=yellow&style=flat-square&logo=github)
- [非常棒的激光雷达地点识别！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/hogyun2/awesome-lidar-place-recognition) ![](https://img.shields.io/github/stars/hogyun2/awesome-lidar-place-recognition?color=yellow&style=flat-square&logo=github)
- [Awesome-LiDAR-MOS ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/neng-wang/Awesome-LiDAR-MOS)![](https://img.shields.io/github/stars/neng-wang/Awesome-LiDAR-MOS?color=yellow&style=flat-square&logo=github)运动物体分割
- [Awesome-LiDAR-Visual-SLAM！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/sjtuyinjie/awesome-LiDAR-Visual-SLAM) ![](https://img.shields.io/github/stars/sjtuyinjie/awesome-LiDAR-Visual-SLAM?color=yellow&style=flat-square&logo=github)
- [很棒的激光雷达！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/szenergy/awesome-lidar)![](https://img.shields.io/github/stars/szenergy/awesome-lidar?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)

## 其他
- [ARHeadsetKit](https://github.com/philipturner/ARHeadsetKit) - 使用 5 美元的 Google Cardboard 来复制 Microsoft Hololens。托管[场景颜色重建]研究的源代码(https://github.com/philipturner/scene-color-reconstruction)。
- [Pointcloudprinter ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/marian42/pointcloudprinter) ![](https://img.shields.io/github/stars/marian42/pointcloudprinter?color=yellow&style=flat-square&logo=github) - 将航空激光雷达扫描的点云数据转换为点云数据的工具用于 3D 打印的实体网格。
- [CloudCompare](https://cloudcompare.org/) - CloudCompare 是一款免费的跨平台点云编辑器软件。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/CloudCompare)![](https://img.shields.io/github/stars/CloudCompare?color=yellow&style=flat-square&logo=github)
- [Pcx ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/keijiro/Pcx) ![](https://img.shields.io/github/stars/keijiro/Pcx?color=yellow&style=flat-square&logo=github) - Unity 的点云导入器/渲染器。
- [Bpy ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/uhlik/bpy) ![](https://img.shields.io/github/stars/uhlik/bpy?color=yellow&style=flat-square&logo=github) - 用于 Blender、点云可视化工具的点云导入器/渲染器/编辑器。
- [语义分割编辑器！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Hitachi-Automotive-And-Industry-Lab/semantic-segmentation-editor) ![](https://img.shields.io/github/stars/Hitachi-Automotive-And-Industry-Lab/semantic-segmentation-editor?color=yellow&style=flat-square&logo=github) - 日立汽车和工业实验室的点云和图像语义分割编辑器，点云注释器/标签。
- [3D 边界框标注工具 ![](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/walzimmer/3d-bat) ![](https://img.shields.io/github/stars/walzimmer/3d-bat?color=yellow&style=flat-square&logo=github) - 3D BAT: A用于全环绕、多模态数据流、点云注释器/标签的半自动、基于 Web 的 3D 注释工具箱。
- [纸！[](https://img.shields.io/badge/paper-blue?style=flat-square&logo=semanticscholar)](https://arxiv.org/pdf/1905.00525.pdf)
- [YouTube 视频！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=gSGG4Lw8BSU)
- [摄影测量导入器！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/SBCV/Blender-Addon-Photogrammetry-Importer) ![](https://img.shields.io/github/stars/SBCV/Blender-Addon-Photogrammetry-Importer?color=yellow&style=flat-square&logo=github) - Blender 插件，用于导入多个库的重建结果。
- [Foxglove](https://foxglove.dev/) - Foxglove Studio 是一款集成的机器人可视化和诊断工具，可以在浏览器中使用，也可以在 Linux、Windows 和 macOS 上作为桌面应用程序下载。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/foxglove/studio)![](https://img.shields.io/github/stars/foxglove/studio?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 频道！[](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/channel/UCrIbrBxb9HBAnlhbx2QycsA)
- [Lichtblick suite](https://github.com/lichtblick-suite) - Lichtblick 是 Foxglove Studio 的开源替代品，用于可视化和分析机器人数据。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/lichtblick-suite/lichtblick)![](https://img.shields.io/github/stars/lichtblick-suite/lichtblick?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [Rerun](https://rerun.io/) - Rerun 是一个用于时间感知多模式数据堆栈和可视化的工具。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/rerun-io/rerun)![](https://img.shields.io/github/stars/rerun-io/rerun?color=yellow&style=flat-square&logo=github) ![](https://img.shields.io/badge/ROS-2-34aec5?style=flat-square&logo=ros)
- [YouTube 频道 ![](https://img.shields.io/badge/youtube-red?style=flat-square&logo=youtube)](https://www.youtube.com/@rerundotio/videos)
- [MeshLab](https://www.meshlab.net/) - MeshLab 是一个开源、可移植且可扩展的系统，用于处理和编辑 3D 三角形网格和点云。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/cnr-isti-vclab/meshlab)![](https://img.shields.io/github/stars/cnr-isti-vclab/meshlab?color=yellow&style=flat-square&logo=github)
- [CloudPeek](https://github.com/Geekgineer/CloudPeek) 是一款轻量级、C++ 单头、跨平台点云查看器，旨在简单高效，无需依赖 PCL 或 Open3D 等繁重的外部库。
- [GitHub存储库！[](https://img.shields.io/badge/github-black?style=flat-square&logo=github)](https://github.com/Geekgineer/CloudPeek)![](https://img.shields.io/github/stars/Geekgineer/CloudPeek?color=yellow&style=flat-square&logo=github)
- [我应该选择哪种 SLAM 算法？](https://www.slambotics.org/blog/which-slam-to-choose) Slambotics - 选择正确的 SLAM 算法

<img src="img/lidar02.svg" alt="LIDAR" />
<img src="https://raw.githubusercontent.com/szenergy/awesome-lidar/refs/heads/main/img/cc0.svg" align="center" width="400" alt="CC0" />
