<template>
  <div id="container" @click="toAmap">{{ initMap }}</div>
</template>

<script>
import AMapLoader from '@amap/amap-jsapi-loader';
import { shallowRef } from '@vue/reactivity'
export default {
  name: 'MapComponent',
  setup(){
  const map = shallowRef(null);
    return{
       map,
    }
  },
  methods:{
    initMap(){
      AMapLoader.load({
        key:"4742216123f6ad9602207f138dea916f",             // 申请好的Web端开发者Key，首次调用 load 时必填
        version:"2.0",      // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
        plugins:[''],       // 需要使用的的插件列表，如比例尺'AMap.Scale'等
      }).then((AMap)=>{
          this.map = new AMap.Map("container",{  //设置地图容器id
            viewMode:"2D",    //是否为3D地图模式
            zoom:12,           //初始化地图级别
            center:[121.498586, 31.239637], //初始化地图中心点位置
          });
      }).catch(e=>{
        console.log(e);
      })
    },
    toAmap(){
      window.location.href = "https://surl.amap.com/1Z44oAFd3oO"
    }
  },
  mounted(){
    //DOM初始化完成进行地图初始化
    this.initMap();
  }
}
</script>

<style  scoped>
#container{
  margin: 10px auto 10px auto;
  width: 100%;
  height: 200px;
  /*position: absolute;
  top: 0; left: 0; bottom: 0; right: 0;*/
}
</style>