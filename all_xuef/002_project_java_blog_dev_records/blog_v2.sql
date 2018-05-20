
/*
创建数据库
*/
CREATE DATABASE blog_v2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

/*

 Source Server         : 
 Source Server Type    : MySQL
 Source Server Version : 50173
 Source Host           : 
 Source Database       : blog_v2

 Target Server Type    : MySQL
 Target Server Version : 50173
 File Encoding         : utf-8

 Date: 05/19/2018
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user`(用户)
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '姓名',
  `username` varchar(20) NOT NULL COMMENT '账号',
  `head_url` varchar(255) NOT NULL COMMENT '头像',
  `salt` varchar(20),
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` int(1),
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

insert into user(name, username, head_url, password, email) values('xuef', 'xuef1991', '...', '121314', '643472092@qq.com');

-- ----------------------------
--  Table structure for `role`(权限)
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(2),
  `name` varchar(20),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

insert into role(user_id, name) values(10, 'ROLE_USER');
insert into role(user_id, name) values(10, 'ROLE_ADMIN');

-- ----------------------------
--  Table structure for `blog`(博客)
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `catalog_id` int(11),
  `user_id` int(11),
  `title` varchar(256) NOT NULL,
  `summary` varchar(1024) NOT NULL,
  `tags` varchar(256) NOT NULL,
  `content` longtext NOT NULL,
  `html_content` longtext NOT NULL,
  `comment_count` int(11) COMMENT '评论数量',
  `read_count` int(11),
  `like_count` int(11),
  `status` int(1),
  `create_time` timestamp DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- ----------------------------
--  Table structure for `comment`(评论)
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `entity_id` int(11),
  `entity_type` int(11),
  `content` text NOT NULL,
  `score` int(11) COMMENT '评论质量',
  `status` int(1),
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `catalog`(博客类别)
-- ----------------------------
DROP TABLE IF EXISTS `catalog`;
CREATE TABLE `catalog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `status` int(1),
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- ----------------------------
--  Table structure for `message`(站内信)
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `status` int(1),
  `conversation_id` varchar(20) COMMENT '消息所属会话',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


