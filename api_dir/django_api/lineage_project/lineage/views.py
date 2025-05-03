# lineage/views.py

from django.http import JsonResponse
from .models import JobLineage


def get_job_lineage(request, job_name):
    try:
        # Try to retrieve the job by job_name
        job = JobLineage.objects.get(job_name=job_name)

        # Return the job's data as a JSON response
        return JsonResponse({
            'job_name': job.job_name,
            'upstream': job.upstream,
            'downstream': job.downstream
        })
    except JobLineage.DoesNotExist:
        # If job doesn't exist, return error message
        return JsonResponse({'error': 'Job not found'}, status=404)
