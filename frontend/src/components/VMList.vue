<template>
  <div>
    <h2>VM List</h2>
    <ul>
      <li v-for="vm in vms" :key="vm.id">
        {{ vm.name }} ({{ vm.status }})
      </li>
    </ul>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
const vms = ref([])
const fetchVMs = async () => {
  const res = await axios.get('/vms/')
  vms.value = res.data
}
onMounted(fetchVMs)
</script>
<style scoped>
</style>
