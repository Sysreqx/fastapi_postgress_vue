<template>
<div>
    <div class="position-absolute d-flex align-items-center my-2 col-12">
        <div class="col-2">
            <img class="col-5" alt="GosuLogo" src="../assets/logoBlue.png">
        </div>
        <div class="col my-2">

        </div>
        <div class="col-2 text-end d-flex align-items-center justify-content-evenly pe-5">
            <div class="d-inline-block" >
                <h5>kaz</h5>
            </div>
            <div class="d-inline-block">
                <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
                </div>
            </div>
            <div class="d-inline-block me-2">
                <h5>ru</h5>
            </div>
        </div>
    </div>
    <div class="height container-fluid d-flex flex-column align-items-center justify-content-center"> 
        <div class="col-11">  
            <div class="btn bg-primary bg-opacity-50 col-xl-3 col-5 py-4 px-3">
                <img class="col-3 mb-3" src="..\assets\image1.png" alt="">
                <h4>Настройка оборудования</h4>
            </div>
        </div>    
        <div class="card col-5 bg-primary bg-opacity-50 mt-5 px-5">
            <form class="p-5 text-start">
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Укажите название магазина или торговой точки:</label>
                    <input type="text" class="form-control" id="exampleFormControlInput1">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput2" class="form-label">Укажите контактный телефон:</label>
                    <input type="number" class="form-control" id="exampleFormControlInput2" placeholder="8(777)777-77-77">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlSelect" class="form-label">Укажите приоритет:</label>
                    <select class="form-select mb-3" id="exampleFormControlInput1" aria-label="select">
                        <option selected disabled> </option>
                        <option value="1">Срочно</option>
                        <option value="2">Как можно скорее</option>
                        <option value="3">До дэдлайна</option>
                    </select>
                </div>
                <div class="form-floating">
                    <a class="btn btn-primary col-12 text-uppercase fs-6 fw-bolder py-2" id="login" @click="createtask">СОЗДАТЬ ЗАЯВКУ</a>
                </div>
            </form>
        </div>
    </div>
</div>
</template>
<script scoped>
    // import HeaderOne from "@/components/HeaderOne.vue";
    
    export default{
        components:{
            // HeaderOne,
        },
        methods:{
            async createtask(){
                this.$router.push({name:'table'});
            },
        }
    }
    </script>
