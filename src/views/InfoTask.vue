<template>
<div>
    <div id="height"></div>
    <HeaderOne />
    <div class="py-5"></div>
    <div class="container-fluid d-flex flex-column align-items-center">
        <div class="col-11 text-start">
            <div class="text-light mx-4 mb-5 mt-3">
                <div class=""><h2>Ошибки при работе с 1С</h2></div>
            </div>
            <div class="row m-0">
                <div class="col-8">
                    <div class="card bg-light mb-5">
                        <div class="card-body pb-0">
                            <h4 class="card-title border-bottom pb-2"> Задача №97455</h4>
                            <h5 class="card-text border-bottom py-4">Здесь будет какое-то описание про задачу. Здесь будет какое-то описание про задачу. Здесь будет какое-то описание про задачу. Здесь будет какое-то описание про задачу. Здесь будет какое-то описание про задачу. </h5>
                            <div class="card-subtitle position-relative d-flex py-2">
                                <input id="addfile" type="file" hidden="hidden" @click="addNewFile">
                                <label class="btn p-0 m-0" for="addfile" id="addfile-btn">
                                    <!-- <i class="bi bi-paperclip h4 d-inline-block"></i> -->
                                    <h5 class="m-0 text-secondary my-auto d-inline-block" id="addfile-text">+ прикрепить файл</h5> 
                                </label>
                            </div>
                        </div>
                        
                        <div class="card-footer bg-transparent py-3">
                            <button class="btn bg-primary bg-opacity-50 text-primary fw-bolder">Сохранить</button>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Коментарии: 0</h4>
                            <input type="text" class="form-control">
                        </div>
                    </div>
                    <div class="mt-5">
                        <button class="btn bg-primary text-light">     <h5>Отменить заявку</h5> </button>
                        <button class="btn bg-light text-primary mx-3"><h5>Закрыть заявку</h5> </button>
                    </div>
                </div>
                <div class="col-4 bg-Success">
                    <div class="card">
                        <div class="card-title bg-primary rounded-top py-4"> </div>
                        <div class="card-body rounded-bottom">
                            <div class="row border-bottom py-2">
                                <div class="col text-secondary">Поставлена:</div>
                                <div class="col"><input type="date"></div>
                            </div>
                            <div class="row border-bottom py-2">
                                <div class="col text-secondary">Исполнитель:</div>
                                <div class="col">Калиева Дильназ</div>
                            </div>
                            <div class="row border-bottom py-2">
                                <div class="col text-secondary">Приоритет:</div>
                                <div class="col">Критический</div>
                            </div>
                            <div class="row py-2">
                                <div class="col text-secondary">Статус:</div>
                                <div class="col">В работе</div>
                            </div>
                            <div class="row border-top py-2 pt-4 d-flex justify-content-around">
                                <button class="btn col-5 bg-primary text-light">Взять в работу</button>
                                <button class="btn col-5 bg-primary bg-opacity-25 text-primary">Закрыть предв.</button>
                            </div>
                        </div>
                    </div>
                    <div class="card card-time bg-primary text-light mt-4">
                        <div class="card-body pb-0">
                            <div class="card-title">Время с момента подачи заявки:</div>
                            <h4><input class="form-control bg-transparent" type="time" value="15:12"></h4>
                        </div>
                        <div class="card-body">
                            <div class="card-title">Время с момента принятия заявки:</div>
                            <h4><input class="form-control bg-transparent" type="time" value="15:12"></h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>
</template>

<script>
import HeaderOne from '@/components/HeaderOne.vue'

export default{
    components:{
        HeaderOne
    },
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
        }
    }
}
</script>


<style scoped>
.card-time .form-control{
    color: rgb(255, 255, 255);
    font-size: 24px;
}
</style>