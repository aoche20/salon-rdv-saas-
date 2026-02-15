<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

const phone_number = ref("");
const password = ref("");

const router = useRouter();
const auth = useAuthStore();

const submit = async () => {
  try {
    await auth.login(phone_number.value, password.value);
    router.push("/dashboard"); // redirection vers dashboard
  } catch (err) {
    console.error(err);
    alert("Identifiants incorrects");
  }
};
</script>

<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">Connexion Propriétaire</h1>

    <input
      v-model="phone_number"
      placeholder="Numéro de téléphone"
      class="w-full p-2 mb-2 border rounded"
    />
    <input
      v-model="password"
      type="password"
      placeholder="Mot de passe"
      class="w-full p-2 mb-2 border rounded"
    />

    <button
      @click="submit"
      class="w-full mt-4 p-3 bg-blue-600 text-white rounded"
    >
      Se connecter
    </button>
  </div>
</template>
