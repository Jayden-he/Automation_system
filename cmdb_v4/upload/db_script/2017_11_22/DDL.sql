/*
Navicat MySQL Data Transfer

Source Server         : 10.83.14.218
Source Server Version : 50719
Source Host           : 10.83.14.218:3306
Source Database       : bqtddb

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2017-10-31 21:03:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bqtd_applicant_information
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_applicant_information`;
CREATE TABLE `bqtd_applicant_information` (
  `id` int(8) NOT NULL,
  `products_type_no` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品类型编号',
  `application_materials_en` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请人需要填写的资料英文',
  `application_materials` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请人需要填写的资料',
  `applicant_type` int(2) DEFAULT NULL COMMENT '申请类型（1：申请人，2：担保人）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_card_info
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_card_info`;
CREATE TABLE `bqtd_card_info` (
  `id` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '姓名',
  `ethnic` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '民族',
  `cardid` varchar(21) COLLATE utf8_unicode_ci NOT NULL COMMENT '身份证号码',
  `birth_date` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '出生日期',
  `province` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '省份',
  `county` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '区县镇',
  `address` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '住址',
  `authority` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '公安局',
  `expiry_date` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '失效日期',
  `cardfront_url` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '身份证正面',
  `cardback_url` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '身份证反面',
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `pk_index` (`cardid`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_facerecognition
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_facerecognition`;
CREATE TABLE `bqtd_facerecognition` (
  `id` int(8) NOT NULL COMMENT 'ID',
  `serial_no` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '合同号',
  `customer_id` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '客户编号',
  `customer_name` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '客户姓名',
  `cert_id` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '身份证',
  `realImage_path` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '现场照片路径',
  `cert_card_image_path` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '身份证照片路径',
  `id5_image_path` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'ID5照片路径',
  `last_real_image_path` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '上次现场照路径',
  `channel_type` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '数据同步渠道类型',
  `short_name` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '外围渠道简称',
  `longitude` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '经度',
  `latitude` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '纬度',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `modified_time` timestamp NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_facerecognition_log
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_facerecognition_log`;
CREATE TABLE `bqtd_facerecognition_log` (
  `id` int(8) NOT NULL COMMENT '主键',
  `serial_no` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '合同号',
  `channel_type` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '渠道类型',
  `short_name` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '外围渠道简称',
  `status_code` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '状态码',
  `msg` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '说明',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_facerecognition_results
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_facerecognition_results`;
CREATE TABLE `bqtd_facerecognition_results` (
  `id` int(8) NOT NULL COMMENT 'ID',
  `contract_no` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '合同号',
  `channel` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '识别渠道',
  `similarity_with_sq` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '现场照/ID5照',
  `similarity_with_qf` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '现场照/身份证照',
  `similarity_with_qq` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '现场照/上次现场照',
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `modified_time` timestamp NULL DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_financial_products
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_financial_products`;
CREATE TABLE `bqtd_financial_products` (
  `id` int(8) NOT NULL COMMENT '主键',
  `products_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品名称',
  `products_type_no` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品类型编号',
  `createtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_products_name` (`products_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_financial_products_dictionaries
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_financial_products_dictionaries`;
CREATE TABLE `bqtd_financial_products_dictionaries` (
  `id` int(8) NOT NULL,
  `products_type_no` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品类型编号',
  `products_type_name` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品类型名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_loan_say
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_loan_say`;
CREATE TABLE `bqtd_loan_say` (
  `id` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(10) COLLATE utf8_unicode_ci NOT NULL COMMENT '类型(1回租  2正租)',
  `orders` int(3) DEFAULT NULL COMMENT '展示顺序',
  `businessName` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '产品名称',
  `quota` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '额度',
  `term` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '期限',
  `depicted` text COLLATE utf8_unicode_ci COMMENT '首付比例',
  `updated_data` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `planOne` text CHARACTER SET utf8 COMMENT '正租产品方案1',
  `planTwo` text CHARACTER SET utf8 COMMENT '正租产品方案2',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_sys_code
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_code`;
CREATE TABLE `bqtd_sys_code` (
  `code_no` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '编码',
  `item_no` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '编号',
  `item_name` varchar(50) COLLATE utf8_bin DEFAULT NULL COMMENT '名称',
  `IS_USE` int(1) DEFAULT NULL COMMENT '是否在使用中（1、使用中，2、停用）',
  `CREATE_USER` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '创建人',
  `CREATE_TIME` datetime DEFAULT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '修改人',
  `UPDATE_TIME` datetime DEFAULT NULL COMMENT '修改时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Table structure for bqtd_sys_contract
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_contract`;
CREATE TABLE `bqtd_sys_contract` (
  `id` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '申请单ID',
  `product_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品类型（01 融资租赁; 02 融资租赁2 ;05 正租）',
  `product_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品名称',
  `product_code` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '产品编码',
  `business_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '业务类型',
  `car_type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆类型 (2 新车 1 二手车)',
  `car_brand` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆品牌',
  `car_brand_id` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆品牌id',
  `oldcar_yeas` int(11) DEFAULT NULL COMMENT '二手车年份',
  `price` decimal(15,4) DEFAULT NULL COMMENT '价格',
  `customer_type` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '客户类型（03个人、05企业）',
  `customer_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '客户名称',
  `document_type` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '证件类型 Ent02	营业执照 Ind01	身份证 Ind02	户口簿 Ind03	护照 Ind04	军官证 Ind05	士兵证 Ind06	港澳居民来往内地通行证 Ind07	台湾同胞来往内地通行证 Ind08	临时身份证 Ind09	外国人居留证 Ind10	警官证 Ind11	其他个人证件  Ind12	香港身份证 Ind13	澳门身份证 Ind14	台湾身份证',
  `document_number` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '证件号码',
  `agree_socialCredit_code` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '统一社会信用代码',
  `phone_number` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '手机号码',
  `is_marry` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '婚姻状态 （1 未婚 2 已婚 3 离异 4 丧偶）',
  `what_industry` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '行业类型  A 农、林、牧、渔业   B 采矿业    C 制造业     D	电力、燃气及水的生产和供应业      E	建筑业    F	交通运输、仓储和邮政业    G	信息传输、计算机服务和软件业  H	批发和零售业  I	住宿和餐饮业  J	金融业    K	房地产业  L	租赁和商务服务业  M	科学研究、技术服务和地质勘查业    N	水利、环境和公共设施管理业    O	居民服务和其他服务业  P	教育  Q	卫生、社会保障和社会福利业    R	文化、体育和娱乐业    S	公共管理和社会组织    T	国际组织  Z	待定',
  `positional_title` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '职称 （1 高级 2 中级 3 初级 0 无 9 未知）',
  `is_creditCard` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '是否有信用卡  (0 没有 1 有)',
  `down_payment` decimal(10,4) DEFAULT NULL COMMENT '保证金/首付',
  `periods` int(11) DEFAULT NULL COMMENT '期数',
  `is_guarantee` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '是否有担保人  (0 没有 1 有)',
  `guarantee_name` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人姓名',
  `guarantee_id` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人身份证ID',
  `guarantee_phoneNo` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人手机号码',
  `longitude` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '经度',
  `latitude` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '纬度',
  `city` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '城市',
  `is_delete` int(11) DEFAULT NULL COMMENT '是否删除 (0 正常 -1 已删除)',
  `apply_userid` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请人ID',
  `finance_manager` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '金融经理',
  `status` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请单状态 1 未提交 0 已提交',
  `apply_date` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请日期',
  `apply_time` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请时间',
  `custome_relation_type` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人与客户之间的关系 1	配偶  2	父亲  3	母亲  4	直系亲属  5	非直系亲属    6	同事  7	朋友 99	其他',
  `customer_id` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '客户ID',
  `update_time` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '修改时间',
  `contract_no` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '合同号',
  `finance_manager_id` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '金融经理ID',
  `sno` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '展厅号',
  `car_seriesname` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车系名称',
  `car_seriescode` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车系编码',
  `car_describe` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆中文描述',
  `car_code` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆型号代码',
  `car_age` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车龄',
  `car_registerDate` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车龄注册日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='申请单表';

-- ----------------------------
-- Table structure for bqtd_sys_contract_attach
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_contract_attach`;
CREATE TABLE `bqtd_sys_contract_attach` (
  `id` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `apply_id` varchar(32) COLLATE utf8_unicode_ci NOT NULL COMMENT '申请ID',
  `card_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '身份证正面',
  `cardback_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '身份证反面',
  `drive_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '驾驶证',
  `bank_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '银行卡',
  `apply_image` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请人照片',
  `apply_witness_image` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '申请人与见证人照片',
  `risk_remind` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '反欺诈风险提示',
  `credit_warrant` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '征信授权书',
  `vehicle_register` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆登记证',
  `vehicle_drive` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆行驶证',
  `drive_image` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '车辆照片',
  `bank_flow` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '个人银行流水',
  `house_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '房产证',
  `company_License` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '公司营业执照',
  `Lease_contract` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '租赁合同',
  `field_scene` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '经营场地现场照片',
  `Detailed` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '对公流水',
  `count_drive` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '库存车辆信息',
  `decision_book` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '股东会决议书',
  `finance_tab` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '财务报表',
  `company_rules` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '公司章程',
  `enterprise_credit` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '企业征信',
  `field_Lease_contract` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '场地租赁合同',
  `business_contract` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '购销合同',
  `taxes_tab` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '纳税申请表',
  `grt_cardid` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人身份证',
  `grt_risk_remind` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人反欺诈风险提示',
  `grt_credit_warrant` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人征信授权书',
  `grt_image` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人照片',
  `grt_drive_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人驾驶证',
  `grt_bank_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人银行卡',
  `grt_witness` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人与见证人照片',
  `grt_vehicle_id` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人车辆登记证',
  `grt_vehicle_drive` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人行驶证',
  `grt_drive` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人车辆照片',
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `credit_apply_tab` varchar(200) COLLATE utf8_unicode_ci DEFAULT '' COMMENT '工行信用卡申请表',
  `by_company_license` varchar(200) CHARACTER SET utf8 DEFAULT NULL COMMENT '挂靠公司营业执照',
  `enterprise_image` varchar(200) CHARACTER SET utf8 DEFAULT NULL COMMENT '企业证照',
  `apply_tab` varchar(200) CHARACTER SET utf8 DEFAULT NULL COMMENT '申请表',
  `grt_bank_flow` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人个人银行流水',
  `grt_house_confirm` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人房产证明',
  `grt_address_confirm` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '担保人住址证明',
  `special_certificate` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '特殊证照',
  `shareholders_authorize` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '股东会授权书',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for bqtd_sys_faq
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_faq`;
CREATE TABLE `bqtd_sys_faq` (
  `id` int(11) NOT NULL,
  `no` int(11) DEFAULT NULL COMMENT '序号',
  `title` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '标题',
  `content` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '内容',
  `creation_time` datetime DEFAULT NULL COMMENT '创建时间',
  `creation_user` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '创建人',
  PRIMARY KEY (`id`),
  UNIQUE KEY `pk_sys_faq` (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_sys_role
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_role`;
CREATE TABLE `bqtd_sys_role` (
  `ID` varchar(32) CHARACTER SET utf8 NOT NULL,
  `role_code` varchar(32) DEFAULT NULL,
  `role_name` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `creation_time` datetime DEFAULT NULL,
  `creation_user` varchar(32) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `update_user` varchar(32) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bqtd_sys_user
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_user`;
CREATE TABLE `bqtd_sys_user` (
  `ID` varchar(32) CHARACTER SET utf8 NOT NULL COMMENT '主键',
  `username` varchar(50) DEFAULT NULL COMMENT '用户名',
  `password` varchar(32) DEFAULT NULL COMMENT '密码',
  `sex` int(11) DEFAULT NULL COMMENT '性别',
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '真实姓名',
  `mail_address` varchar(50) DEFAULT NULL COMMENT '邮箱地址',
  `phone_number` varchar(11) DEFAULT NULL COMMENT '手机号码',
  `ID_number` varchar(18) DEFAULT NULL COMMENT '身份证号码',
  `head_img_url` varchar(50) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '头像地址',
  `creatrttime` datetime DEFAULT NULL COMMENT '创建人',
  `user_status` int(11) DEFAULT NULL COMMENT '用户状态',
  `contract_d` int(11) DEFAULT NULL COMMENT '个人业绩--天',
  `contract_m` int(11) DEFAULT NULL COMMENT '个人业绩--月',
  `providers_code` varchar(32) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '经销商编码',
  `providers_name` varchar(100) CHARACTER SET utf8 DEFAULT NULL COMMENT '经销商名称',
  `store_code` varchar(32) CHARACTER SET utf8 DEFAULT NULL COMMENT '展厅编码',
  `store_name` varchar(100) CHARACTER SET utf8 DEFAULT NULL COMMENT '展厅名称',
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bqtd_sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_sys_user_role`;
CREATE TABLE `bqtd_sys_user_role` (
  `roleid` int(11) NOT NULL COMMENT '主键',
  `role_code` varchar(255) DEFAULT NULL COMMENT '角色编码',
  `userid` int(11) DEFAULT NULL COMMENT '用户id',
  `creation_time` datetime DEFAULT NULL COMMENT '创建时间',
  `creation_user` varchar(32) DEFAULT NULL COMMENT '创建人',
  `update_time` datetime DEFAULT NULL COMMENT '修改时间',
  `update_user` varchar(32) DEFAULT NULL COMMENT '修改人',
  `status` int(11) DEFAULT NULL COMMENT '状态',
  PRIMARY KEY (`roleid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bqtd_ui_index_banner
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_ui_index_banner`;
CREATE TABLE `bqtd_ui_index_banner` (
  `id` bigint(20) unsigned NOT NULL COMMENT '主键',
  `bannerimage` varchar(64) DEFAULT NULL COMMENT '广告图的路径+名称',
  `bannerurl` varchar(200) DEFAULT NULL COMMENT '广告图链接的路径地址',
  `describle` varchar(200) DEFAULT NULL COMMENT '广告描述',
  `is_use` tinyint(3) unsigned DEFAULT NULL COMMENT '启用标准(1---启用,0—已关闭)',
  `sort` bigint(20) unsigned DEFAULT NULL COMMENT '排序（小到大）',
  `gmt_create` datetime DEFAULT NULL COMMENT '创建时间',
  `gmt_modified` datetime DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bqtd_user_feedback
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_user_feedback`;
CREATE TABLE `bqtd_user_feedback` (
  `fbid` varchar(32) CHARACTER SET utf8 NOT NULL COMMENT '主键',
  `feedback_userid` varchar(32) CHARACTER SET utf8 DEFAULT NULL COMMENT '反馈人ID',
  `feedback_content` varchar(200) CHARACTER SET utf8 DEFAULT NULL COMMENT '反馈内容',
  `feedback_time` datetime DEFAULT NULL COMMENT '反馈时间',
  `feedback_versions` varchar(12) CHARACTER SET utf8 DEFAULT NULL COMMENT '反馈针对版本',
  `feedback_status` int(11) DEFAULT NULL COMMENT '反馈状态1：有效 2：无效'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bqtd_user_loginlog
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_user_loginlog`;
CREATE TABLE `bqtd_user_loginlog` (
  `logid` varchar(32) COLLATE utf8_unicode_ci NOT NULL COMMENT '主键',
  `userid` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '用户id',
  `imei` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '设备唯一编码',
  `logintime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '登陆时间',
  `longitude` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '经度',
  `latitude` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '纬度',
  PRIMARY KEY (`logid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Table structure for bqtd_user_message
-- ----------------------------
DROP TABLE IF EXISTS `bqtd_user_message`;
CREATE TABLE `bqtd_user_message` (
  `ID` varchar(32) NOT NULL COMMENT '主键',
  `recipients` varchar(32) DEFAULT NULL COMMENT '收件人',
  `sender` varchar(32) DEFAULT NULL COMMENT '发送人',
  `message_content` varchar(200) DEFAULT NULL COMMENT '信息内容',
  `send_time` datetime DEFAULT NULL COMMENT '发送时间',
  `message_status` int(11) DEFAULT NULL COMMENT '信息状态',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
