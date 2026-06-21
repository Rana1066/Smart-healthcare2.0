import { Component } from '@angular/core';
import { Navbar } from '../../components/navbar/navbar';
import { Treatment } from '../../services/treatment';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-treatments',
  imports: [CommonModule,Navbar],
  templateUrl: './treatments.html',
  styleUrl: './treatments.css',
})
export class Treatments {
treatments: any[] = [];

  constructor(
    private treatmentService: Treatment
  ) {}

  ngOnInit(): void {
    this.loadTreatments();
  }

  loadTreatments() {

    this.treatmentService
      .getTreatments()
      .subscribe({
        next: (data: any) => {
          this.treatments = data;
        },
        error: (error) => {
          console.log(error);
        }
      });
  }
}
