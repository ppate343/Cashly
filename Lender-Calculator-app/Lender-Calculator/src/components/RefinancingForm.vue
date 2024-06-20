<template>
    <div class="refinancing-form">
      <h2>Refinancing Form</h2>
      <div class="form-group">
        <label for="refinanceType">Refinance Type</label>
        <select v-model="form.refinanceType" id="refinanceType">
          <option value="refinance1st">Refinance 1st</option>
          <option value="refinance2nd">Refinance 2nd</option>
        </select>
      </div>

      <div class="form-group">
        <label for="mortgageAmount">Mortgage Amount</label>
        <input type="number" v-model.number="form.mortgageAmount" id="mortgageAmount" />
      </div>
      <div class="form-group">
        <label for="mortgageAmountNeeded">Mortgage Amount Needed</label>
        <input type="number" v-model.number="form.mortgageAmountNeeded" id="mortgageAmountNeeded" />
      </div>
      <div class="form-group">
        <label for="propertyValue">Property Value</label>
        <input type="number" v-model.number="form.propertyValue" id="propertyValue" />
      </div>
      <div class="form-group">
        <label for="creditScore">Credit Score</label>
        <input type="number" v-model.number="form.creditScore" id="creditScore" />
      </div>
      <div class="form-group">
        <label for="monthlyHouseExpenses">Monthly House Expenses</label>
        <input type="number" v-model.number="form.monthlyHouseExpenses" id="monthlyHouseExpenses" />
        <button @click="addExpense">+</button>
      </div>
      <div class="total-expenses">
        Total Monthly House Expenses: {{ form.monthlyHouseExpenses }}
      </div>
      <div class="form-group">
        <label for="additionalDetails">Additional Details</label>
        <input type="text" v-model="form.additionalDetails" id="additionalDetails" />
        <button @click="addExpense">+</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RefinancingForm',
    data() {
      return {
        form: {
          refinanceType: '',
          mortgageAmount: 0,
          mortgageAmountNeeded: 0,
          propertyValue: 0,
          creditScore: 0,
          monthlyHouseExpenses: 0
        }
      };
    },
    methods: {
      addExpense() {
        const additionalExpense = parseFloat(prompt('Enter additional expense:'));
        if (!isNaN(additionalExpense)) {
          this.form.monthlyHouseExpenses += additionalExpense;
        }
      }
    }
  };
  </script>
  
  <style>
  .refinancing-form {
    max-width: 500px;
    margin: 0 auto;
    text-align: left;
  }
  .form-group {
    margin-bottom: 15px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input, select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  button {
    padding: 8px 12px;
    margin-top: 5px;
    background-color: blue;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: darkblue;
  }
  .total-expenses {
    margin-top: 20px;
    font-weight: bold;
  }
  </style>
  