from typing import List
from dataclasses import dataclass

@dataclass
class Daily_Note_expeditions:
    avatar_side_icon: str  # 头像icon
    status: str  # 'Finished' or 'Ongoing' 状态
    remained_time: str  # 剩余时间

@dataclass
class Transformer_Recovery_Time:
    Day: int
    Hour: int 
    Minute: int
    Second: int
    reached: bool

@dataclass
class Transformer:
    obtained: str # 是否获得
    recovery_time: Transformer_Recovery_Time
    wiki: str

@dataclass
class Daily_Note_Info:
    current_resin: int  # 当前树脂
    max_resin: int  # 最大树脂
    resin_recovery_time: str  # 树脂回复时间
    finished_task_num: int  # 完成委托个数
    total_task_num: int  # 全部委托个数
    is_extra_task_reward_received: bool
    remain_resin_discount_num: int  # 周本树脂减半剩余次数
    resin_discount_num_limit: int  # 周本树脂减半次数
    current_expedition_num: int  # 当前派遣数量
    max_expedition_num: int  # 最大派遣数量
    expeditions: List[Daily_Note_expeditions]  # 派遣列表
    current_home_coin: int # 当前洞天宝钱
    max_home_coin: int # 最大洞天宝钱
    home_coin_recovery_time: int # 洞天宝钱回复时间
    calendar_url: str
    transformer: Transformer # 参量质变仪