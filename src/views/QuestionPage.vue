<template>
<div>
    <div class="position-absolute col-12 row d-flex align-items-center">
        <div class="col-3">
            <img class="col-3" alt="GosuLogo" src="../assets/logoBlue.png">
        </div>
        <div class="col"></div>
        <div class="col-2 text-end d-flex align-items-center justify-content-evenly px-5">
            <div class="d-inline-block" >
                <h5>kaz</h5>
            </div>
            <div class="d-inline-block">
                <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
                </div>
            </div>
            <div class="d-inline-block">
                <h5>ru</h5>
            </div>
        </div>
    </div>
    <div class="height container-fluid d-flex flex-column align-items-center justify-content-center"> 
        <div class="col-11">  
            <div class="btn bg-primary bg-opacity-50 col-3 pb-4 px-3">
                <img class="col-4" src="..\assets\image2.png" alt="">
                <h4>Вопрос по 1С</h4>
            </div>
        </div>    
        <div class="card col-5 bg-primary bg-opacity-50 mt-5 px-5">
            <form class="p-5 text-start">
                <div class="mb-3">
                    <label for="exampleFormControlSelect1" class="form-label">Выберите из списка примерный вариант вопроса:</label>
                    <select class="form-select mb-3" id="exampleFormControlSelect1" aria-label="Default select example">
                        <option selected disabled> </option>
                        <option value="1">Создание пользователя</option>
                        <option value="2">Настройка отчёта</option>
                        <option value="3">Нет цен</option>
                        <option value="1">Проблемы с себестоимостью</option>
                        <option value="2">Вопрос по бухгалтерии</option>
                        <option value="3">Вопрос по ЗУПу</option>
                        <option value="1">Изменить неверный документ</option>
                        <option value="2">Новое техническое задание</option>
                        <option value="3">Не закрывается смена</option>
                        <option value="3">Ничего не подходит</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlSelect" class="form-label">Укажите приоритет:</label>
                    <select class="form-select mb-3" id="exampleFormControlSelect" aria-label="Default select example">
                        <option selected disabled> </option>
                        <option value="1">Обычная</option>
                        <option value="2" class="bg-warning bg-opacity-50">Высокий</option>
                        <option value="3" class="bg-danger bg-opacity-50">Критический</option>
                    </select>
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
                    <a class="btn btn-primary col-12 text-uppercase fs-6 fw-bolder py-2" id="login" @click="createQuestion">СОЗДАТЬ ЗАЯВКУ</a>
                </div>
            </form>
        </div>
    </div>
</div>
</template>

<style scoped>
</style>

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
        async createQuestion(){
            this.$router.push({name: 'table'})
        }
    }
}
</script>