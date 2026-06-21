import { HttpClient, HttpHeaders } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Appointment {
   private http = inject(HttpClient);
  getAppointments() {

  const token =
    localStorage.getItem('access_token');

  const headers = new HttpHeaders({
    Authorization: `Bearer ${token}`
  });

  return this.http.get(
    'http://127.0.0.1:8000/api/appointments/',
    { headers }
  );
}
}
