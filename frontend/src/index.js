import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { Provider } from 'react-redux';
import { store } from './store/store';

// Inject Google Inter Font
const link = document.createElement('link');
link.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap';
link.rel = 'stylesheet';
document.head.appendChild(link);

// Apply font to body
document.body.style.fontFamily = "'Inter', sans-serif";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);