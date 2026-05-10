<template>
  <div class="vm-list">
    <h2>VM List</h2>
    <button @click="showCreateForm = true">Create VM</button>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>CPU</th>
          <th>Memory (GB)</th>
          <th>Storage (GB)</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="vm in vms" :key="vm.id">
          <td>{{ vm.id }}</td>
          <td>{{ vm.name }}</td>
          <td>{{ vm.cpu }}</td>
          <td>{{ vm.memory }}</td>
          <td>{{ vm.storage }}</td>
          <td>
            <button @click="deleteVM(vm.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <VMForm v-if="showCreateForm" @created="fetchVMs" @close="showCreateForm = false" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import VMForm from './VMForm.vue';

const vms = ref([]);
const showCreateForm = ref(false);

const fetchVMs = async () => {
  try {
    const res = await axios.get('/api/vms');
    vms.value = res.data;
  } catch (e) {
    console.error('Failed to fetch VMs', e);
  }
};

const deleteVM = async (id) => {
  if (!confirm('Delete VM?')) return;
  try {
    await axios.delete(`/api/vms/${id}`);
    fetchVMs();
  } catch (e) {
    console.error('Delete failed', e);
  }
};

onMounted(fetchVMs);
</script>

<style scoped>
.vm-list {
  margin-top: 20px;
}
.vm-list table {
  width: 100%;
  border-collapse: collapse;
}
.vm-list th, .vm-list td {
  border: 1px solid #ddd;
  padding: 8px;
}
.vm-list th {
  background-color: #f2f2f2;
}
</style>