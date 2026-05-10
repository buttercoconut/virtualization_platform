<template>
  <div class="vm-form">
    <h3>Create VM</h3>
    <form @submit.prevent="createVM">
      <label>Name: <input v-model="name" required /></label>
      <label>CPU: <input type="number" v-model.number="cpu" min="1" required /></label>
      <label>Memory (GB): <input type="number" v-model.number="memory" min="1" required /></label>
      <label>Storage (GB): <input type="number" v-model.number="storage" min="10" required /></label>
      <div class="actions">
        <button type="submit">Create</button>
        <button type="button" @click="close">Cancel</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const emit = defineEmits(['created', 'close']);
const name = ref('');
const cpu = ref(2);
const memory = ref(4);
const storage = ref(20);

const createVM = async () => {
  try {
    await axios.post('/api/vms', {
      name: name.value,
      cpu: cpu.value,
      memory: memory.value,
      storage: storage.value,
    });
    emit('created');
    close();
  } catch (e) {
    console.error('Create VM failed', e);
  }
};

const close = () => {
  emit('close');
};
</script>

<style scoped>
.vm-form {
  border: 1px solid #ccc;
  padding: 15px;
  margin-top: 15px;
}
.vm-form label {
  display: block;
  margin-bottom: 8px;
}
.vm-form .actions {
  margin-top: 10px;
}
.vm-form button {
  margin-right: 5px;
}
</style>