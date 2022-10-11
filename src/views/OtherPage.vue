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
                <img class="col-3 mb-3" src="..\assets\image3.png" alt="">
                <h4>Другое</h4>
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
                    <label for="exampleFormControlTextarea1" class="form-label">Опишите проблему:</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="2"></textarea>
                </div>
                <div class="mb-3 position-relative d-flex">
                    <input id="addfile" type="file" hidden="hidden" @click="addNewFile">
                    <label class="btn p-0 m-0" for="addfile" id="addfile-btn">
                        <i class="bi bi-paperclip h4 d-inline-block"></i>
                        <h5 class="m-0 text-secondary my-auto d-inline-block" id="addfile-text">Файл</h5> 
                    </label>
                </div>
                <div class="form-floating">
                    <a class="btn btn-primary col-12 text-uppercase fs-6 fw-bolder py-2" id="login" @click="createOther">СОЗДАТЬ ЗАЯВКУ</a>
                </div>
            </form>
        </div>
    </div>
</div>
</template>

<script>
    export default{
        methods:{
            async addNewFile(){
                const addfile = document.getElementById("addfile");
                // const btn = document.getElementById("addfile-btn");
                const text = document.getElementById("addfile-text");
            
                addfile.addEventListener("change", function(){
                    if(addfile.value){
                        text.innerText = addfile.value.split('\\').pop().split('/').pop();
                    }
                    else{
                        text.innerText = "Файл не выбран";
                    }
                })
            },
            async createOther(){
                this.$router.push({name: 'table'})
            }
        }
    }
    </script>