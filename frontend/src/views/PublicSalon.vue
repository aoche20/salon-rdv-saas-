<script setup>
import { ref, onMounted } from "vue";
import http from "../api/http";
import { useBookingStore } from "../stores/booking";
import { useRouter, useRoute } from "vue-router";

const store = useBookingStore();
const router = useRouter();
const route = useRoute();

const services = ref([]);
const slots = ref([]);
const selectedDate = ref("");

onMounted(async () => {
  const res = await http.get(`salons/${route.params.id}/`);
  store.salon = res.data;

  const servicesRes = await http.get("services/");
  services.value = servicesRes.data;
});

const selectService = async (service) => {
  store.service = service;

  const res = await http.get("available-slots/", {
    params: {
      employee: 1, // MVP
      service: service.id,
      date: selectedDate.value,
    },
  });

  slots.value = res.data.slots;
};

const selectSlot = (slot) => {
  store.slot = slot;
  store.date = selectedDate.value;
  router.push("/confirm");
};
</script>

<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">{{ store.salon?.name }}</h1>

    <input
      type="date"
      v-model="selectedDate"
      class="w-full p-2 border rounded mb-4"
    />

    <div v-for="service in services" :key="service.id" class="mb-3">
      <button
        class="w-full p-3 bg-black text-white rounded"
        @click="selectService(service)"
      >
        {{ service.name }} – {{ service.price_fcfa }} FCFA
      </button>
    </div>

    <div class="grid grid-cols-2 gap-2 mt-4">
      <button
        v-for="slot in slots"
        :key="slot.start"
        class="p-2 border rounded"
        @click="selectSlot(slot)"
      >
        {{ slot.start }} - {{ slot.end }}
      </button>
    </div>
  </div>
</template>
