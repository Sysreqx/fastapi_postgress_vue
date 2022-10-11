<template>
<div>
<HeaderOne />
<div id="height"></div>
<div class="height container-fluid d-flex flex-column align-items-center justify-content-center">
    <div class="col-11">
        <div class="mb-3 d-flex">
            <div class="col-4 bg-light rounded d-flex align-items-center px-2 py-2 me-5">
                <h1 class="text-primary">125 &ensp;</h1><h3>закрытых заявок</h3>
            </div>
            <div class="col-4 bg-light rounded d-flex align-items-center px-2 py-2">
                <h1 class="text-primary">84 &ensp;</h1><h3>заявок в работе</h3>
            </div>
        </div>
        <div class="card">
            <table class="table bg-light text-start">
                <thead class="fw-bolder text-light">
                <tr class=" bg-primary rounded-3">
                    <th scope="col">ID</th>
                    <th scope="col">Тема</th>
                    <th scope="col">Наименование</th>
                    <th scope="col">Исполнитель</th>
                    <th scope="col">Дата подачи заявки</th>
                    <th scope="col">Приоритет</th>
                    <th scope="col">Статус</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td class="btn" @click="task">Askona</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-07-22" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td>Damiana</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-10-02" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Ошибки при работе с 1С</td>
                    <td>Вопрос по ЗУПу</td>
                    <td>Не назначено</td>
                    <td><input class="bg-transparent border-0" type="date" value="2022-09-30" min="2022-01-01" max="2032-12-31"></td>
                    <td>Критический</td>
                    <td>В работе</td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
</div>
</template>
<script scoped>
import HeaderOne from "@/components/HeaderOne.vue";

export default{
    components:{
        HeaderOne,
    },
    methods:{
        async task(){
            this.$router.push({name: 'info'});
        }
    }
}
</script>
<style>
</style>