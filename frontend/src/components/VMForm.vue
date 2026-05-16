<template>
  <div>
    <h2>VM Form</h2>
    <form @submit.prevent="createVM">
      <input v-model="name" placeholder="Name" required />
      <input v-model.number="cpu" type="number" placeholder="CPU" required />
      <input v-model.number="memory" type="number" placeholder="Memory (MB)" required />
      <input v-model.number="storage" type="number" placeholder="Storage (GB)" required />
      <input v-model.number="host_id" type="number" placeholder="Host ID" required />
      <button type="submit">Create</button>
    </form>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import axios from 'axios'
const name = ref('')
const cpu = ref(1)
const memory = ref(1024)
const storage = ref(20)
const host_id = ref(1)
const createVM = async () => {
  await axios.post('/vms/', { name, cpu, memory, storage, host_id })
  window.location.reload()
}
</script>
