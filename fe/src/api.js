import axios from 'axios';

const api = axios.create({
  // baseURL: '//www.moyui.me/api/',
  baseURL: '/api/',
  method: 'get',
  timeout: 3000,
  withCredentials: true,
  responseType: 'json'
});

export default function(input) {
  const { url = '', method, data = {}, params = {} } = input;
  return new Promise((resolve, reject) => {
    api({ url, method, data, params })
      .then(res => {
        if ((res.status >= 200 && res.status < 300) || res.status == 301) {
          return resolve(res.data);
        } else {
          return reject(res);
        }
      })
      .catch(rej => reject(rej.response));
  });
}
