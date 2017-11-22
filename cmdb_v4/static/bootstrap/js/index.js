$(document).ready(function(){
	//$("#left-menu>li ul").hide();	
	$("#left-menu>li:first ul").slideDown();
	addBC4A();

	//默认选中基础信息	
	$("#start-tomcat").trigger("click");
	$("#start-tomcat").attr("style", "background-color:#D8D8D8");
});

function addBC4A(){
	//click菜单，改变背景颜色
	$("#left-menu a[class*='menuitem']").click(function(){		
				$("#left-menu a[class*='menuitem']").removeAttr("style");
				$(this).attr("style", "background-color:#D8D8D8");
			}
		);

	//菜单的缩放
	$("#left-menu a").click(
			function(event){
				//debugger;
				$(this).parents('li').first().siblings().children('ul').slideUp();
				$(this).parent().children().slideDown();
				//$(this).parent().hasClass("")
				//避免连接默认事件的执行
				event.preventDefault();
			}
	);
	
	
	$("#tomcat a[class*='menuitem']").click(
			function(){
				$("#top-tab-div").hide();
				var menutext = $(this).text();
				switch (menutext){

					case '服务器管理':
						$("#contentframe").attr("src", "/restart_tomcat_page");
						break;
					case '机房管理':
						$("#contentframe").attr("src", "/start_tomcat_page");
						break;
					case '系统管理':
						$("#contentframe").attr("src", "/stop_tomcat_page");
						break;
					case '项目管理':
						$("#contentframe").attr("src", "/war_page");
						break;
				}
			}
	);
	
	
	
	
	
	
	
	
}
