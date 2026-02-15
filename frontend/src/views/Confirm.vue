<script setup>
import { ref } from "vue";
import http from "../api/http";
import { useBookingStore } from "../stores/booking";

// Store Pinia
const store = useBookingStore();

// WhatsApp helper
const whatsappLink = (phone, message) =>
  `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;

const openWhatsapp = (phone, message) => {
  const link = whatsappLink(phone, message);
  window.open(link, "_blank");
};

// Création RDV
const confirm = async () => {
  try {
    const payload = {
      salon: store.salon.id,
      service: store.service.id,
      employee: 1, // MVP : 1 seul employé ou sélection à venir
      client_name: "Client WhatsApp", // pourrait être input futur
      client_phone: "22901030516",    // pourrait être input futur
      date: store.date,
      start_time: store.slot.start,
      end_time: store.slot.end,
      status: "confirmed",
    };

    await http.post("appointments/", payload);

    // Message WhatsApp automatique
    const message = `Bonjour, votre rendez-vous est confirmé ✅
📅 Date : ${store.date}
⏰ Heure : ${store.slot.start} - ${store.slot.end}
💇 Service : ${store.service.name}
📍 Salon : ${store.salon.name}`;
    openWhatsapp(payload.client_phone, message);

    alert("Rendez-vous confirmé ! WhatsApp ouvert.");
  } catch (err) {
    console.error(err);
    alert("Impossible de créer le rendez-vous");
  }
};
</script>

<template>
  <div class="p-4">
    <h2 class="text-lg font-bold mb-4">Confirmation du rendez-vous</h2>

    <p>📍 Salon : {{ store.salon.name }}</p>
    <p>💇 Service : {{ store.service.name }}</p>
    <p>📅 Date : {{ store.date }}</p>
    <p>⏰ Heure : {{ store.slot.start }} - {{ store.slot.end }}</p>

    <button
      class="w-full mt-6 p-3 bg-green-600 text-white rounded text-lg"
      @click="confirm"
    >
      Confirmer le rendez-vous & WhatsApp
    </button>
  </div>
</template>

<style scoped>
body {
  font-family: sans-serif;
  background-color: #f5f5f5;
}
</style>
