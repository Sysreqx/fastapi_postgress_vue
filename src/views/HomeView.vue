<template>
  <div class="about">
    <div class="height container-fluid d-flex flex-column align-items-center justify-content-center">
      <div class="home align-items-center">
        <img class="col-2 col-xxl-2" alt="GosuLogo" src="../assets/logoBlue.png">
        <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
      </div>
      <div class="col-2 m-3 d-flex justify-content-evenly fs-4">
        <router-link to="#">Қаз</router-link>
        <router-link to="#">Рус</router-link>
      </div>
      <div><h4>Выберите интересующий вас раздел:</h4></div>
      <div class="col-11 d-flex justify-content-evenly mt-5 pb-5">
        <div class="btn bg-primary bg-opacity-50 col-3 py-4 px-3" @click="setting">
          <img class="col-3 mb-3" src="..\assets\image1.png" alt="">
          <h4>Настройка оборудования</h4>
        </div>
        <div class="btn bg-primary bg-opacity-50 col-3 py-4 px-3" @click="question">
          <img class="col-3 mb-3" src="..\assets\image2.png" alt="">
          <h4>Вопрос по 1С</h4>
        </div>
      </div>
      <div class="col-11 d-flex justify-content-evenly mb-5 pb-5">
        <div class="btn bg-primary bg-opacity-50 col-3 py-4 px-3" @click="other">
          <img class="col-3 mb-3" src="..\assets\image3.png" alt="">
          <h4>Другое</h4>
        </div>
        <div class="btn bg-primary bg-opacity-50 col-3 py-4 px-3" @click="allTask">
          <img class="col-3 mb-3" src="..\assets\image4.png" alt="">
          <h4>Все заявки</h4>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
  name: 'HomeView',
  components: {
    // HelloWorld
  },
  methods:{
    async setting(){
      this.$router.push({name:'setting'});
    },
    async question(){
      this.$router.push({name:'question'});
    },
    async other(){
      this.$router.push({name:'other'});
    },
    async allTask(){
      this.$router.push({name:'table'});
    }
  }
}
</script>