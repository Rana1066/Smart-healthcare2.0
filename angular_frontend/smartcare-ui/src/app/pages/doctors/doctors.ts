import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Doctor } from '../../services/doctor';
import { Navbar } from '../../components/navbar/navbar';

@Component({
  selector: 'app-doctors',
  imports: [CommonModule,Navbar],
  templateUrl: './doctors.html',
  styleUrl: './doctors.css',
})
export class Doctors {
  doctors: any[] = [];

  constructor(
    private doctorService: Doctor
  ) {}

  ngOnInit(): void {
    this.loadDoctors();
  }

  loadDoctors() {
    this.doctorService
      .getDoctors()
      .subscribe({
        next: (data: any) => {
          this.doctors = data;
        }
      });
  }
}
