const base = {
    get() {
        return {
            url : "http://localhost:8080/django5v380/",
            name: "django5v380",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于python的健身房管理系统"
        } 
    }
}
export default base
