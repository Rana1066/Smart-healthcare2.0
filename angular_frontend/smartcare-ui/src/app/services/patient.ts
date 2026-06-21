import { HttpClient, HttpHeaders } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Patient {
  private http = inject(HttpClient);

  apiUrl = 'http://127.0.0.1:8000/api/patients/';

  getPatients(): Observable<any> {

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
