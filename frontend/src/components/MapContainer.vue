<template>
  <div id="wrap" v-touch="toAmap">
    <tr>
      <td><img src="../assets/pin.png" id="locate_icon" alt="Fender Rhodes" align="center"></td>
      <td id="locationdescription">【北京市盈科（深圳）律师事务所】<br/>深圳市福田区鹏程一路广电金融中心30-32层</td>
    </tr>
  </div>
  <div id="container" v-touch="toAmap">
    {{ initMap }}
  </div>
</template>

<script>
import AMapLoader from '@amap/amap-jsapi-loader';
import { shallowRef } from '@vue/reactivity';
export default {
  name: 'MapComponent',
  setup(){
  const map = shallowRef(null);
    return{
       map,
       ShowPage: false
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
            zoom:17,           //初始化地图级别
            center:[114.050778, 22.541596], //初始化地图中心点位置
          });
          var marker = new AMap.Marker({
          position: new AMap.LngLat(114.050778, 22.541596),
          title: '北京市盈科（深圳）律师事务所',
          label: { 
            content: '北京市盈科（深圳）律师事务所',
            direction: 'top'
          },
          });
      this.map.add(marker)
      }).catch(e=>{
        // eslint-disable-next-line
        console.log(e);
      });
    },
    toAmap(){
      window.location.href = "https://surl.amap.com/pFQHCsq109xd"
    },
  },
  mounted(){
    //DOM初始化完成进行地图初始化
    this.initMap();
  }
}
</script>

<style  scoped>
#container{
  width: 100%;
  height: 200px;
  cursor: pointer
}

#wrap{
  cursor: pointer;
}

#locate_icon{
  height: 2em;
}

#locationdescription{
  text-align: left;
}
</style>