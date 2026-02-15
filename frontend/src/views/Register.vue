<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

const phone_number = ref("");
const fullname = ref("");
const password = ref("");
const router = useRouter();
const auth = useAuthStore();

const submit = async () => {
  try {
    await auth.register(phone_number.value, fullname.value, password.value);
    alert("Compte créé ! Connectez-vous maintenant.");
    router.push("/login");
  } catch (err) {
    console.error(err);
    alert("Erreur inscription");
  }
};
</script>

<template>
  <div>
    <h1>Inscription Propriétaire</h1>
    <input v-model="fullname" placeholder="Nom complet" />
    <input v-model="phone_number" placeholder="Téléphone" />
    <input v-model="password" type="password" placeholder="Mot de passe" />
    <button @click="submit">S’inscrire</button>
  </div>
</template>
