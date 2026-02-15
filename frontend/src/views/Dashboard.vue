<script setup>
import { ref, onMounted } from "vue";
import http from "../api/http";
import { useAuthStore } from "../stores/auth";
import { useRouter } from "vue-router";
const auth = useAuthStore();
const router = useRouter();

// utilitaire WhatsApp
const whatsappLink = (phone, message) =>
  `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
const openWhatsapp = (phone, message) => {
  const link = whatsappLink(phone, message);
  window.open(link, "_blank");
};

// état
const date = ref(new Date().toISOString().slice(0, 10));
const appointments = ref([]);

// charger RDV du jour
const loadAppointments = async () => {
  try {
    const res = await http.get("appointments/", {
      params: { date: date.value },
    });
    appointments.value = res.data;
  } catch (err) {
    console.error(err);
    alert("Impossible de charger les rendez-vous");
  }
};

// changer statut d’un RDV + WhatsApp
const updateStatus = async (rdv, status) => {
  try {
    await http.patch(`appointments/${rdv.id}/status/`, { status });
    loadAppointments();

    if (status === "confirmed") {
      const message = `Bonjour ${rdv.client_name}, votre rendez-vous est confirmé pour aujourd’hui à ${rdv.start_time}. Salon: ${rdv.salon_name}`;
      openWhatsapp(rdv.client_phone, message);
    }
  } catch (err) {
    console.error(err);
    alert("Impossible de mettre à jour le rendez-vous");
  }
};

onMounted(loadAppointments);
const logoutUser = () => {
  auth.logout();
  router.push("/login");
};
</script>

<template>
  <div class="p-4 bg-gray-100 min-h-screen">
  <button
    @click="logoutUser"
    class="bg-red-600 hover:bg-red-700 text-white font-bold px-4 py-2 rounded shadow"
  >
    Déconnexion
  </button>
    <h1 class="text-2xl font-bold mb-6 text-gray-800 flex items-center gap-2">
      📅 Agenda du jour
    </h1>

    <div class="mb-6 flex justify-center">
      <input
        type="date"
        v-model="date"
        @change="loadAppointments"
        class="p-3 rounded-lg border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
    </div>

    <div class="grid gap-4">
      <div
        v-for="rdv in appointments"
        :key="rdv.id"
        class="bg-white p-4 rounded-2xl shadow-lg hover:shadow-2xl transition duration-300"
      >
        <div class="flex justify-between items-center mb-2">
          <span class="text-lg font-semibold text-gray-700">{{ rdv.start_time }} - {{ rdv.end_time }}</span>
          <span
            class="px-2 py-1 rounded-full text-sm font-medium"
            :class="{
              'bg-green-100 text-green-700': rdv.status === 'confirmed',
              'bg-red-100 text-red-700': rdv.status === 'cancelled',
              'bg-yellow-100 text-yellow-700': rdv.status === 'pending'
            }"
          >
            {{ rdv.status }}
          </span>
        </div>

        <p class="text-gray-800 font-medium">{{ rdv.client_name }} • {{ rdv.client_phone }}</p>
        <p class="text-gray-500 text-sm">{{ rdv.service_name }} • {{ rdv.salon_name }}</p>

        <div class="flex gap-3 mt-4">
          <button
            class="flex-1 bg-green-600 hover:bg-green-700 text-white font-semibold p-2 rounded-xl shadow-md transition"
            @click="updateStatus(rdv, 'confirmed')"
          >
            Confirmer & WhatsApp
          </button>

          <button
            class="flex-1 bg-red-600 hover:bg-red-700 text-white font-semibold p-2 rounded-xl shadow-md transition"
            @click="updateStatus(rdv, 'cancelled')"
          >
            Annuler
          </button>
        </div>
      </div>
    </div>

    <p v-if="appointments.length === 0" class="text-center text-gray-400 mt-8">
      Aucun rendez-vous aujourd’hui
    </p>
  </div>
</template>

<style scoped>
/* Optional: petite animation sur hover des cartes */
div[v-for] {
  transform: translateY(0);
  transition: transform 0.2s;
}
div[v-for]:hover {
  transform: translateY(-3px);
}
</style>
