import { HttpClient, HttpHeaders } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Treatment {
  private http = inject(HttpClient);

  apiUrl = 'http://127.0.0.1:8000/api/treatments/';

  getTreatments() {

    const token = localStorage.getItem('access_token');

    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`
    });

    return this.http.get(
      this.apiUrl,
      { headers }
    );
  }
}
