job_skills = ['frontend', 'react', 'cloud', 'google', 'backend', 'officebased']
applicant_requirements = ['development', 'coding', 'workfromhome', 'cloud', 'backend']

def match_skills(job_skill_list, applicant_reqs_list):
    # Determine the total number of job_skills to match 100% for the role
    skills_len = len(job_skill_list)

    # Go through the list if skills required for the job and match them against the applicants requirements
    # If any match then store them in the matched_skills list

    matched_skills = []
    for skill in job_skill_list:
        matched_skills += [ app_skill for app_skill in applicant_reqs_list if skill in app_skill ]

    # Workout the score by dividing the no.of matched skills against the total job skills required
    # and mulitple by 100 to get a percentage value

    #Make sure values a unique in the list
    matched_set = set(matched_skills)

    # Get the unique set of values in the matched skills list
    matched_skills_len = len(matched_set)

    #Finally work out the score and return the value.
    return round((matched_skills_len/skills_len)*100)

#Run the function
print('Score:', match_skills(job_skills, applicant_requirements))


