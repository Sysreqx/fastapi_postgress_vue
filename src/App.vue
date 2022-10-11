<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <router-view/>
</template>

<style>
#app {
  text-align: center;
}
:root{
  --bs-primary: #65B2F0;
  --bs-primary-rgb: 101,178,240;
}
.btn-primary {
    --bs-btn-bg: #65B2F0;
    --bs-btn-border-color: #65B2F0;
    --bs-btn-hover-bg: #4b9adb;
    --bs-btn-hover-border-color: #4593d3;
    --bs-btn-active-bg: #4593d3;
    --bs-btn-active-border-color: #4593d3;
    --bs-btn-disabled-bg: #65B2F0;
    --bs-btn-disabled-border-color: #65B2F0;
}
.height{
  height: 100vh;
}
a{
  color: black;
  text-decoration: none;
}
a:-webkit-any-link {
    color: black;
    cursor: pointer;
    text-decoration: none;
}
 #height{
    background-color: rgb(101, 177, 240, 0.5);
    width: 100%;
    height: 100vh;
    position: fixed;
    z-index: -2;
 }
</style>
