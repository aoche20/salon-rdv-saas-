import { defineStore } from "pinia";

export const useBookingStore = defineStore("booking", {
  state: () => ({
    salon: null,
    service: null,
    employee: null,
    date: null,
    slot: null,
  }),
});
