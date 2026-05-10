<template>
  <div class="app-container">
    <h1>Virtualization Platform Dashboard</h1>
    <VMList />
  </div>
</template>

<script setup>
import VMList from './components/VMList.vue';
</script>

<style scoped>
.app-container {
  padding: 20px;
  font-family: Arial, sans-serif;
}
</style>