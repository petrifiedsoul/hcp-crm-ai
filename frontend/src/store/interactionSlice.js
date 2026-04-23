import { createSlice } from '@reduxjs/toolkit';

const interactionSlice = createSlice({
  name: 'interaction',
  initialState: {
    formData: {
      hcpName: '',
      date: '',
      topics: '',
      sentiment: '',
      materials: ''
    }
  },
  reducers: {
    updateForm: (state, action) => {
      const incomingData = action.payload;
      
      // Loop through the AI's extracted data
      Object.keys(incomingData).forEach(key => {
        // ONLY update the form if the AI actually found new data for that specific field
        if (incomingData[key] !== "" && incomingData[key] !== null && incomingData[key] !== "Unknown") {
          state.formData[key] = incomingData[key];
        }
      });
    }
  }
});

export const { updateForm } = interactionSlice.actions;
export default interactionSlice.reducer;