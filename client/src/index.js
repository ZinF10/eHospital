import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from '@/App';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux';
import { store } from '@/redux/store';
import Loading from '@/components/common/Loading';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <React.Suspense fallback={<Loading />}>
      <Provider store={store}>
        <App />
      </Provider>
    </React.Suspense>
  </React.StrictMode>
);

reportWebVitals();